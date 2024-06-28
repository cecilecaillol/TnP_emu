from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "SingleElectron_2017E"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_Electron_Data_2017.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/SingleElectron/Run2017E-UL2017_MiniAODv2-v1/MINIAOD" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/TnP_el_2017/"
#config.Data.outLFNDirBase = "/store/group/cmst3/user/ccaillol/reNanoAOD/"
config.Data.outputDatasetTag = "TnP_ntuples_el2017"
config.Data.inputDBS = "global"
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 500
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
