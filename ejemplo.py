# Databricks notebook source
#invocar a otras librerias SQL
from pyspark.sql import SQLContext

sqlContext = SQLContext(spark.sparkContext)
