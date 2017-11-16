# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys
import json
import yaml
import regex
from copy import copy
import datetime
from collections import namedtuple, defaultdict
import inspect
import functools
import glob
import numpy as np

import xlrd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Font

from pandas import DataFrame
import pandas as pd
import pdb

from explay.utils import is_buildin, replace_str, to_yml
from explay.openpyxl_ext import insert_rows
from explay.parser import xlParser, xlBinaryParser
from explay.merger import xlMerger

from explay.utils import register_func
from explay.agg_func import agg_functions
from explay.post_func import common_funcs


register_func()


def compose(*functions):
    def compose2(f, g):
        return lambda x: f(g(x))
    return functools.reduce(compose2, functions, lambda x: x)


class xlRenderer():
    def __init__(self, params):
        self.first_row, self.idx_colname = params['first_row'], params['idx_colname']

    @classmethod
    def to_excel(cls, df, path):
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        datetime_format = workbook.add_format({'num_format': "yyyy-mm-dd"})
        time_format = workbook.add_format({'num_format': "hh:mm"})

        for index, values in df.iterrows():
            for i, v in enumerate(values):
                if type(v) == pd.Timestamp:
                    worksheet.write_datetime('%s%s' % (chr(65+i), index + 2), v, datetime_format)
                elif type(v) == datetime.time:
                    cell = '%s%s' % (chr(65+i), index+2)
                    worksheet.write_datetime('%s%s' % (chr(65+i), index + 2), v, time_format)
        writer.save()

    def render_excel(self, df, saved_name, template_name):

        xls_file, xlsx_file = ['template/%s.%s' % (template_name, ext) for ext in ['xls', 'xlsx']]
        template = load_workbook(xlsx_file)

        rows = dataframe_to_rows(df, index=True, header=False)
        ws = template.active
        ws.insert_rows = insert_rows

        ws.insert_rows(ws, self.first_row, len(df))
        xls_from = xlrd.open_workbook(xls_file, formatting_info=True)
        xls_sheet = xls_from.sheet_by_index(0)
        color_index = lambda row, col: (
            xls_from.xf_list[xls_sheet.cell_xf_index(row,col)].background.pattern_colour_index)
        rgb = lambda row, col: xls_from.colour_map[color_index(row,col)]
        to_hexcode = lambda rgb_code: '00%s' % ''.join([('%x'% e).upper() for e in rgb_code])

        get_cell = lambda sht, row, col: sht['%s%d' % (get_column_letter(col), row)]

        for r_idx, row in enumerate(rows, self.first_row):
            for c_idx, df_colname in self.idx_colname.items():
                col_idx = df.columns.get_loc(df_colname)
                get_cell(ws, r_idx, c_idx).value = row[col_idx+1]

        for row in ws.rows:
            max_contents_len = []
            for cell in row:
                r_idx, c_idx = cell.row, cell.col_idx

                max_content_len = len(str(get_cell(ws, r_idx, c_idx)))
                max_contents_len.append(max_content_len)

                #  if cell.has_style:
                new_cell = get_cell(ws, r_idx, c_idx)

                if r_idx >= self.first_row:
                    font = get_cell(ws, self.first_row, c_idx).font
                else:
                    font = cell.font
                new_cell.font = copy(font)
                new_cell.border = copy(cell.border)

                # uses xlrd to get cell styles
                if r_idx < self.first_row:
                    color = to_hexcode(rgb(r_idx-1, c_idx-1))
                else:
                    color = to_hexcode(rgb(self.first_row-1, c_idx-1))
                fill = PatternFill(fill_type='solid',start_color=color)
                new_cell.fill = copy(fill)

                new_cell.number_format = cell.number_format
                new_cell.protection = copy(cell.protection)
                new_cell.alignment = copy(cell.alignment)

        template.save(saved_name)
        print('{} saved'.format(saved_name))


class xlManager():

    def __init__(self, yml_file, home=None, local_imported=None):
        home = os.getcwd() if not home else home
        yml_path = '%s/%s' % (home, yml_file)
        self.yml, self.home = yml_path, home
        self.sources = dict()
        self.content = _c = to_yml(yml_file, True)
        self.converter = _c['xlconverter']
        self.parser = _c['xlparser']
        self.variables = _c['variables']

        self.load_parser()
        if local_imported:
            self.import_local(local_imported)

    def load_parser(self):
        parsers = {}
        for each in self.parser:
            print('\n')
            name = each['name']
            each_parser = None
            each = defaultdict(str, each)
            each_parser = xlBinaryParser(each)
            parsers[name] = each_parser
        self.parsers = parsers

    def import_local(self, local):
        for name, obj in self.parsers.items():
            local[name] = obj

    def import_variables(self, local):
        for v, value in self.variables.items():
            local[v] = value

    def register_func(self):
        import func
        #  print('reigister_func')
        funcs = [f for f in dir(func) if f.startswith('exp')]
        for func_name in funcs:
            func_name_in_yml = func_name[4:]
            #  print('func {} registed.'.format(func_name))
            #  print('func name in yml: {}'.format(func_name_in_yml))
            register_custom_func(func_name_in_yml, getattr(func, func_name))

    def load_excel(self, converter_name, filepath, sheet_name=0):
        cv = xlConverter(self.process.converter)
        df = cv.load_excel(converter_name, filepath, sheet_name)
        return df

    def merge_sheets(self, converter_name, filepath, sheet_names):
        source_path = os.path.join(self.home, 'source')
        #  self.merger = xlMerger(self.process.converter, source_path)
        self.merger = xlMerger(self.converter, source_path)
        df_merged = self.merger.merge_sheets(converter_name, filepath, sheet_names)
        self.sources[converter_name] = df_merged
        return df_merged
        #  return self

    def merge_files(self, converter_name, filepaths, sheet_name=0):
        source_path = os.path.join(self.home, 'source')
        #  self.merger = xlMerger(self.process.converter, source_path)
        self.merger = xlMerger(self.converter, source_path)
        df_merged = self.merger.merge_files(converter_name, filepaths, sheet_name)
        self.sources[converter_name] = df_merged
        return df_merged
        #  return self

    def merge_all(self, converter_name, sheet_name=0, filename_excludes=None):
        print(sheet_name, filename_excludes)
        source_path = os.path.join(self.home, 'source')
        #  self.merger = xlMerger(self.process.converter, source_path)
        self.merger = xlMerger(self.converter, source_path)
        df_merged = self.merger.merge_all(converter_name, sheet_name, filename_excludes)
        self.sources[converter_name], files = df_merged
        print('files merged: %s' % ','.join(files))
        return df_merged
        #  return self

    def to_excel(self, saved_path):
        if self.df is not None:
            self.renderer.to_excel(self.df, saved_path)

    def render_excel(self, df, excel_template, saved_path):
        self.renderer.render_excel(df, saved_path, excel_template)
