from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

schema_communities_crime = StructType([
    StructField('state', IntegerType(), True),
    StructField('county', IntegerType(), True),
    StructField('community', IntegerType(), True),
    StructField('communityname', StringType(), True),
    StructField('fold', IntegerType(), True),
    StructField('population', FloatType(), True),
    StructField('householdsize', FloatType(), True),
    StructField('racepctblack', FloatType(),  True),
    StructField('racePctWhite', FloatType(), True),
    StructField('racePctAsian', FloatType(), True),
    StructField('racePctHisp', FloatType(), True),
    StructField('agePct12t21', FloatType(), True),
    StructField('agePct12t29', FloatType(), True),
    StructField('agePct16t24', FloatType(), True),
    StructField('agePct65up', FloatType(), True),
    StructField('numbUrban', FloatType(), True),
    StructField('pctUrban', FloatType(), True),
    StructField('medIncome', FloatType(), True),
    StructField('pctWWage', FloatType(), True),
    StructField('pctWFarmSelf', FloatType(), True),
    StructField('pctWInvInc', FloatType(), True),
    StructField('pctWSocSec', FloatType(), True),
    StructField('pctWPubAsst', FloatType(), True),
    StructField('pctWRetire', FloatType(), True),
    StructField('medFamInc', FloatType(), True),
    StructField('perCapInc', FloatType(), True),
    StructField('whitePerCap', FloatType(), True),
    StructField('blackPerCap', FloatType(), True),
    StructField('indianPerCap', FloatType(), True),
    StructField('AsianPerCap', FloatType(), True),
    StructField('OtherPerCap', FloatType(), True),
    StructField('HispPerCap', FloatType(), True),
    StructField('NumUnderPov', FloatType(), True),
    StructField('PctPopUnderPov', FloatType(), True),
    StructField('PctLess9thGrade', FloatType(), True),
    StructField('PctNotHSGrad', FloatType(), True),
    StructField('PctBSorMore', FloatType(), True),
    StructField('PctUnemployed', FloatType(), True),
    StructField('PctEmploy', FloatType(), True),
    StructField('PctEmplManu', FloatType(), True),
    StructField('PctEmplProfServ', FloatType(), True),
    StructField('PctOccupManu', FloatType(), True),
    StructField('PctOccupMgmtProf', FloatType(), True),
    StructField('MalePctDivorce', FloatType(), True),
    StructField('MalePctNevMarr', FloatType(), True),
    StructField('FemalePctDiv', FloatType(), True),
    StructField('TotalPctDiv', FloatType(), True),
    StructField('PersPerFam', FloatType(), True),
    StructField('PctFam2Par', FloatType(), True),
    StructField('PctKids2Par', FloatType(), True),
    StructField('PctYoungKids2Par', FloatType(), True),
    StructField('PctTeen2Par', FloatType(), True),
    StructField('PctWorkMomYoungKids', FloatType(), True),
    StructField('PctWorkMom', FloatType(), True),
    StructField('NumIlleg', FloatType(), True),
    StructField('PctIlleg', FloatType(), True),
    StructField('NumImmig', FloatType(), True),
    StructField('PctImmigRecent', FloatType(), True),
    StructField('PctImmigRec5', FloatType(), True),
    StructField('PctImmigRec8', FloatType(), True),
    StructField('PctImmigRec10', FloatType(), True),
    StructField('PctRecentImmig', FloatType(), True),
    StructField('PctRecImmig5', FloatType(), True),
    StructField('PctRecImmig8', FloatType(), True),
    StructField('PctRecImmig10', FloatType(), True),
    StructField('PctSpeakEnglOnly', FloatType(), True),
    StructField('PctNotSpeakEnglWell', FloatType(), True),
    StructField('PctLargHouseFam', FloatType(), True),
    StructField('PctLargHouseOccup', FloatType(), True),
    StructField('PersPerOccupHous', FloatType(), True),
    StructField('PersPerOwnOccHous', FloatType(), True),
    StructField('PersPerRentOccHous', FloatType(), True),
    StructField('PctPersOwnOccup', FloatType(), True),
    StructField('PctPersDenseHous', FloatType(), True),
    StructField('PctHousLess3BR', FloatType(), True),
    StructField('MedNumBR', FloatType(), True),
    StructField('HousVacant', FloatType(), True),
    StructField('PctHousOccup', FloatType(), True),
    StructField('PctHousOwnOcc', FloatType(), True),
    StructField('PctVacantBoarded', FloatType(), True),
    StructField('PctVacMore6Mos', FloatType(), True),
    StructField('MedYrHousBuilt', FloatType(), True),
    StructField('PctHousNoPhone', FloatType(), True),
    StructField('PctWOFullPlumb', FloatType(), True),
    StructField('OwnOccLowQuart', FloatType(), True),
    StructField('OwnOccMedVal', FloatType(), True),
    StructField('OwnOccHiQuart', FloatType(), True),
    StructField('RentLowQ', FloatType(), True),
    StructField('RentMedian', FloatType(), True),
    StructField('RentHighQ', FloatType(), True),
    StructField('MedRent', FloatType(), True),
    StructField('MedRentPctHousInc', FloatType(), True),
    StructField('MedOwnCostPctInc', FloatType(), True),
    StructField('MedOwnCostPctIncNoMtg', FloatType(), True),
    StructField('NumInShelters', FloatType(), True),
    StructField('NumStreet', FloatType(), True),
    StructField('PctForeignBorn', FloatType(), True),
    StructField('PctBornSameState', FloatType(), True),
    StructField('PctSameHouse85', FloatType(), True),
    StructField('PctSameCity85', FloatType(), True),
    StructField('PctSameState85', FloatType(), True),
    StructField('LemasSwornFT', FloatType(), True),
    StructField('LemasSwFTPerPop', FloatType(), True),
    StructField('LemasSwFTFieldOps', FloatType(), True),
    StructField('LemasSwFTFieldPerPop', FloatType(), True),
    StructField('LemasTotalReq', FloatType(), True),
    StructField('LemasTotReqPerPop', FloatType(), True),
    StructField('PolicReqPerOffic', FloatType(), True),
    StructField('PolicPerPop', FloatType(), True),
    StructField('RacialMatchCommPol', FloatType(), True),
    StructField('PctPolicWhite', FloatType(), True),
    StructField('PctPolicBlack', FloatType(), True),
    StructField('PctPolicHisp', FloatType(), True),
    StructField('PctPolicAsian', FloatType(), True),
    StructField('PctPolicMinor', FloatType(), True),
    StructField('OfficAssgnDrugUnits', FloatType(), True),
    StructField('NumKindsDrugsSeiz', FloatType(), True),
    StructField('PolicAveOTWorked', FloatType(), True),
    StructField('LandArea', FloatType(), True),
    StructField('PopDens', FloatType(), True),
    StructField('PctUsePubTrans', FloatType(), True),
    StructField('PolicCars', FloatType(), True),
    StructField('PolicOperBudg', FloatType(), True),
    StructField('LemasPctPolicOnPatr', FloatType(), True),
    StructField('LemasGangUnitDeploy', FloatType(), True),
    StructField('LemasPctOfficDrugUn', FloatType(), True),
    StructField('PolicBudgPerPop', FloatType(), True),
    StructField('ViolentCrimesPerPop', FloatType(), True),
])


def check_is_null(col):
    return (F.col(col).isNull())


def pergunta_1(df):
    df = (df.withColumn("PolicOperBudg", F.when(check_is_null('PolicOperBudg'), 0)
                        .otherwise(F.col("PolicOperBudg")))
          )
    (df.groupBy(F.col('state'), F.col('communityname'))
     .agg(F.round(F.sum(F.col('PolicOperBudg')), 2).alias('orcamento_policial'))
     .orderBy(F.col('orcamento_policial').desc())
     .show())


def pergunta_2(df):
    df = (df.withColumn('ViolentCrimesPerPop', F.when(check_is_null('ViolentCrimesPerPop'), 0)
                        .otherwise(F.col('ViolentCrimesPerPop')))
          )
    (df.groupBy(F.col('state'), F.col('communityname'))
     .agg(F.round(F.sum(F.col('ViolentCrimesPerPop')), 2).alias('crimes_violentos'))
     .orderBy(F.col('crimes_violentos').desc())
     .show())


def pergunta_3(df):
    df = (df.withColumn('population', F.when(check_is_null('population'), 0)
                        .otherwise(F.col('population')))
          )
    (df.groupBy(F.col('state'), F.col('communityname'))
     .agg(F.round(F.sum(F.col('population')), 2).alias('populacao'))
     .orderBy(F.col('populacao').desc())
     .show())


def pergunta_4(df):
    df = (df.withColumn('racepctblack', F.when(check_is_null('racepctblack'), 0)
                        .otherwise(F.col('racepctblack')))
          )
    (df.groupBy(F.col('state'), F.col('communityname'))
     .agg(F.round(F.sum(F.col('racepctblack')), 2).alias('populacao_negra'))
     .orderBy(F.col('populacao_negra').desc())
     .show())


def pergunta_5(df):
    df = (df.withColumn('pctWWage', F.when(check_is_null('pctWWage'), 0)
                        .otherwise(F.col('pctWWage')))
          )
    (df.groupBy(F.col('state'), F.col('communityname'))
     .agg(F.round(F.sum(F.col('pctWWage')), 2).alias('renda_salarial'))
     .orderBy(F.col('renda_salarial').desc())
     .show())


def pergunta_6(df):
    df = (df.withColumn('agePct12t29', F.when(check_is_null('agePct12t29'), 0)
                        .otherwise(F.col('agePct12t29')))
          )
    (df.groupBy(F.col('state'), F.col('communityname'))
     .agg(F.round(F.sum(F.col('agePct12t29')), 2).alias('jovens_entre_12_29_anos'))
     .orderBy(F.col('jovens_entre_12_29_anos').desc())
     .limit(1)
     .show()
     )


if __name__ == "__main__":
    sc = SparkContext()
    spark = (SparkSession.builder.appName(
        "Aceleração PySpark - Capgemini [Communities & Crime]"))

    df = (spark.getOrCreate().read
          .format("csv")
          .option("header", "true")
          .schema(schema_communities_crime)
          .load("/home/spark/capgemini-aceleracao-pyspark/data/communities-crime/communities-crime.csv"))

pergunta_1(df)
pergunta_2(df)
pergunta_3(df)
pergunta_4(df)
pergunta_5(df)
pergunta_6(df)
