from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "DYJetsToLL_M-50_2016post"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_Muon_MC_2016post.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/TnP_mu_2016post/"
#config.Data.outLFNDirBase = "/store/group/cmst3/user/ccaillol/reNanoAOD/"
config.Data.outputDatasetTag = "TnP_ntuples_mu2016post"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
