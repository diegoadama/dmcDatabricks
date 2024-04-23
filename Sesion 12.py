# Databricks notebook source
dbutils.widgets.text("fechaProceso","20240422","ParametroFecha")
dbutils.widgets.text("nombreUsuario","Diego","ParametroUsuario")

# COMMAND ----------

fechaProceso = dbutils.widgets.get("fechaProceso")
nombreProceso = dbutils.widgets.get("nombreUsuario")

# COMMAND ----------

print(fechaProceso)
print(nombreProceso)
