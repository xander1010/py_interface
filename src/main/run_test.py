# coding=utf-8
import sys
sys.path.append("..")

from base.run_method import RunMethod
from data.get_data import GetData

class RunTest:
	def __init__(self, ):
		self.run_method = RunMethod()
		self.data = GetData()

	# 程序执行的
	def go_on_run(self):
		rows_count = self.data.get_case_lines()
		for i in (1,rows_count):
