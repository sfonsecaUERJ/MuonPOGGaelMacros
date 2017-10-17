import FWCore.ParameterSet.Config as cms
import os
import sys
args = sys.argv[1:]
# print args
if (sys.argv[0] == "cmsRun"): args =sys.argv[2:]
scenario = "data_all"
if len(args) > 0: scenario = args[0]
print "Will run scenario ", scenario 

### USAGE:
###    cmsRun TriggerEff.py <scenario> [ <id> [ <binning1> ... <binningN> ] ]
###    ex> cmsRun TriggerEff.py mc IsoMu20_from_Tight2012
### scenarios:
###   - data_all (default)  
###   - signal_mc

### newly added variable on top of default TnP tree by using "AddBranch.py":
### [IsoMu24_OR_IsoTkMu24]: IsoMu24 == 1 or IsoTkMu24 == 1
### [Mu50_OR_TkMu50]: Mu50 == 1 or HLT_TkMu50 == 1
### [pair_dPhi]: abs(tag_phi - phi) if abs(tag_phi - phi) < 3.1415926535 else 2*3.1415926535 - abs(tag_phi - phi);tag_eta;eta;phi;tag_phi
### [pair_dPhiPrimeDeg]: pair_dPhi*(180/3.1415926535) if ((tag_eta > 0.9 and eta > 0.9) or (tag_eta < -0.9 and eta < -0.9)) else 999;pair_dPhi;tag_eta;eta;phi;tag_phi

def Add_AdditionalBranches( _PassingProbe, _ProbeCondition):
    # Template.Variables.combRelIsoPF04dBeta = cms.vstring("pf relative isolation", "0", "999", "")

    if _PassingProbe == "DoubleMu20_7_Mass0to30":
        Template.Categories.DoubleMu20_7_Mass0to30 = cms.vstring("DoubleMu20_7_Mass0to30", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "Mu7p5_MU":
        Template.Categories.Mu7p5_MU = cms.vstring("Mu7p5_MU", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "IsoMu20":
        Template.Categories.IsoMu20 = cms.vstring("IsoMu20", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "HLT_Mu17_Photon30_IsoCaloId":
        Template.Categories.HLT_Mu17_Photon30_IsoCaloId = cms.vstring("HLT_Mu17_Photon30_IsoCaloId", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "Mu17_Photon30_IsoCaloId":
        Template.Categories.Mu17_Photon30_IsoCaloId = cms.vstring("Mu17_Photon30_IsoCaloId", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "HLT_DoubleMu20_7_Mass0to30_Photon23":
        Template.Categories.HLT_DoubleMu20_7_Mass0to30_Photon23 = cms.vstring("HLT_DoubleMu20_7_Mass0to30_Photon23", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "HLT_DoubleMu20_7_Mass0to30_L1_DM4":
        Template.Categories.HLT_DoubleMu20_7_Mass0to30_L1_DM4 = cms.vstring("HLT_DoubleMu20_7_Mass0to30_L1_DM4", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")
    
    if _PassingProbe == "HLT_DoubleMu20_7_Mass0to30_L1_DM4EG":
        Template.Categories.HLT_DoubleMu20_7_Mass0to30_L1_DM4EG = cms.vstring("HLT_DoubleMu20_7_Mass0to30_L1_DM4EG", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "IsoMu24":
        Template.Categories.IsoMu24 = cms.vstring("IsoMu24", "dummy[pass=1,fail=0]")
        Template.Categories.HighPt = cms.vstring("HighPt", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")
        Template.Categories.Glb = cms.vstring("Glb", "dummy[pass=1,fail=0]")
        # Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")
        # Template.Variables.combRelIsoPF04dBeta = cms.vstring("pf relative isolation", "0", "999", "")
        # Template.Variables.pair_dPhiPrimeDeg = cms.vstring("pair_dPhiPrimeDeg", "0", "9999", "")
    
    if _PassingProbe == "Tight2012":
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")

    if _PassingProbe == "HighPt":
        Template.Categories.HighPt = cms.vstring("HighPt", "dummy[pass=1,fail=0]")

    if _PassingProbe == "Loose":
        Template.Categories.Loose = cms.vstring("Loose", "dummy[pass=1,fail=0]")
        # Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")
        # Template.Variables.combRelIsoPF04dBeta = cms.vstring("pf relative isolation", "0", "999", "")
        # Template.Variables.pair_dPhiPrimeDeg = cms.vstring("pair_dPhiPrimeDeg", "0", "9999", "")

    elif _PassingProbe == "IsoMu24_OR_IsoTkMu24":
        Template.Categories.IsoMu24_OR_IsoTkMu24 = cms.vstring("IsoMu24_OR_IsoTkMu24", "dummy[pass=1,fail=0]")
        Template.Categories.Tight2012 = cms.vstring("Tight2012", "dummy[pass=1,fail=0]")
        Template.Variables.combRelIsoPF04dBeta = cms.vstring("pf relative isolation", "0", "999", "")
        Template.Variables.pair_dPhiPrimeDeg = cms.vstring("pair_dPhiPrimeDeg", "0", "9999", "")

    elif _PassingProbe == "Mu50_OR_TkMu50":
        Template.Categories.Mu50_OR_TkMu50 = cms.vstring("Mu50_OR_TkMu50", "dummy[pass=1,fail=0]")
        Template.Categories.HighPt = cms.vstring("HighPt", "dummy[pass=1,fail=0]")
        Template.Variables.relTkIso = cms.vstring("Relative Tracker Isolation", "0", "999", "")
        Template.Variables.pair_dPhiPrimeDeg = cms.vstring("pair_dPhiPrimeDeg", "0", "9999", "")


def FindTnPTreeName( BaseLocation, _PassingProbe, _ProbeCondition, accessMethod ):
    # TnPFilesString = cms.vstring(  )
    TnPFilesString = []
    for file in os.listdir(BaseLocation):
        if file.endswith(".root"):
            if accessMethod == "xrootd":
                # fileLocation = "root://cms-xrd-global.cern.ch//store" + os.path.join(BaseLocation, file).split('store', 1 )[1]
                fileLocation = "root://eoscms//eos/cms/store" + os.path.join(BaseLocation, file).split('store', 1 )[1]
                TnPFilesString.append(fileLocation)
            if accessMethod == "local":
                fileLocation = os.path.join(BaseLocation, file)
                TnPFilesString.append(fileLocation)

    # print len(TnPFilesString[:10])
    # return TnPFilesString[:10]
    print len(TnPFilesString)
    return TnPFilesString



PassingProbe = ""
ProbeCondition = ""
# print args
if "_from_" in args[1]:
    PassingProbe = args[1].split("_from_")[0]
    ProbeCondition = args[1].split("_from_")[1]
else:
    PassingProbe = args[1]
    ProbeCondition = "None"

print "PassingProbe: " + PassingProbe
print "On top of " + ProbeCondition

# old
# BaseLocation = "/uscmst1b_scratch/lpc1/3DayLifetime/edacosta/CMSSW_9_2_4/src/MuonAnalysis/TagAndProbe/test/zmumu/crab_MuonEGv1_TagAndProbeNtuples_Run2017D_v3/crab_MuonEGv1/results"
# new
# BaseLocation = "/uscmst1b_scratch/lpc1/3DayLifetime/edacosta/CMSSW_9_2_4/src/MuonAnalysis/TagAndProbe/test/zmumu/crab_MuonEGDv1_TagAndProbeNtuples_Run2017D/crab_MuonEGDv1/results"

BaseLocation = "/eos/cms/store/user/ftorresd/triggerStudies2017/MuonEG_Run2017D-PromptReco-v1_AOD_TnP_Producer_MuonEG_JPsi_v02/MuonEG/MuonEG_Run2017D-PromptReco-v1_AOD/171009_194257/0000/"



# Type = os.getcwd().split("/")[-2] # -- Dir name -- #
Type = "None"


# Ntuple_Data = cms.vstring( "file:"+BaseLocation+"/"+List_TnPTree[0] )
# Ntuple_MC = cms.vstring( "file:"+BaseLocation+"/"+List_TnPTree[1] )
rootTrees = []
BaseLocation = "/eos/cms/store/user/ftorresd/triggerStudies2017/MuonEG_Run2017D-PromptReco-v1_AOD_TnP_Producer_MuonEG_JPsi_v02/MuonEG/MuonEG_Run2017D-PromptReco-v1_AOD/171009_194257/0000/"
rootTrees +=  FindTnPTreeName( BaseLocation, PassingProbe, ProbeCondition, "xrootd" ) 
BaseLocation = "/eos/cms/store/user/ftorresd/triggerStudies2017/MuonEG_Run2017D-PromptReco-v1_AOD_TnP_Producer_MuonEG_JPsi_v02/MuonEG/MuonEG_Run2017D-PromptReco-v1_AOD/171009_194257/0001/"
rootTrees +=  FindTnPTreeName( BaseLocation, PassingProbe, ProbeCondition, "xrootd" ) 
Ntuple_Data = cms.vstring( rootTrees )

# print rootTrees
# for root in rootTrees:
#     Ntuple_Data.append( root )


# Ntuple_Data = FindTnPTreeName( BaseLocation, PassingProbe, ProbeCondition, "xrootd" )
Ntuple_Data = cms.vstring( "tnpJPsi_Data_Skimmed.root" )
# Ntuple_Data = cms.vstring( "root://cms-xrd-global.cern.ch//store/group/phys_muon/TagAndProbe/Run2017/92X-v2_TrkIter/RunD/TnPTree_SingleMuon_Run2017Dv1_302344_to_302654_GoldenJSON.root", "TnPTree_SingleMuon_Run2017Dv1_301998_to_302343_GoldenJSON.root" )
# Ntuple_Data = cms.vstring( "TnPTree_SingleMuon_Run2017Dv1_302344_to_302654_GoldenJSON.root", "TnPTree_SingleMuon_Run2017Dv1_301998_to_302343_GoldenJSON.root" )
# Ntuple_Data = cms.vstring( "TnPTree_SingleMuon_Run2017Dv1_301998_to_302343_GoldenJSON_SKIMMED.root" )
Ntuple_MC = cms.vstring( "" )

# Ntuple_Data = cms.vstring( "file:tnp_Data.root" )
# Ntuple_MC = cms.vstring( "file:tnp_Data.root" )


print "+" * 100;
print "Type: " + Type
print "Data Location: ", Ntuple_Data
print "MC location: ", Ntuple_MC
print "+" * 100;

process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),

    Variables = cms.PSet(
        mass = cms.vstring("Tag-muon Mass", "2.8", "3.4", "GeV/c^{2}"),
        # mass = cms.vstring("Tag-muon Mass", "85", "100", "GeV/c^{2}"),
        pt = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        phi = cms.vstring("muon #phi", "-3.14", "3.14", ""),
        tag_pt = cms.vstring("tag muon p_{T}", "0", "1000", "GeV/c"),
        eta    = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        tag_abseta = cms.vstring("tag muon |#eta|", "0", "2.5", ""),
        tag_nVertices = cms.vstring("Number of vertices", "0", "999", ""),
        pair_deltaR = cms.vstring("pair_deltaR", "0", "999", ""),
        tag_combRelIsoPF04dBeta = cms.vstring("tag_combRelIsoPF04dBeta", "0", "999", ""),
        pair_probeMultiplicity = cms.vstring("multiplicity","0","99",""),
        # pair_drM1   = cms.vstring("#Delta R(Station 1)", "-99999", "999999", "rad"),
        pair_pt = cms.vstring("Dimuon p_{T}", "0", "1000", "GeV/c"),
    ),

    Categories = cms.PSet(
        tag_Mu50 = cms.vstring("tag_Mu50", "dummy[pass=1,fail=0]"),
        tag_Mu_L3 = cms.vstring("Mu_L3", "dummy[pass=1,fail=0]"),
        tag_IsoMu24 = cms.vstring("tag_IsoMu24", "dummy[pass=1,fail=0]"),
        tag_IsoMu20 = cms.vstring("tag_IsoMu20", "dummy[pass=1,fail=0]"),
        tag_Dimuon25_Jpsi = cms.vstring("tag_Dimuon25_Jpsi", "dummy[pass=1,fail=0]"),
        tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q = cms.vstring("tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q", "dummy[pass=1,fail=0]"),
        tag_Mu7p5_MU = cms.vstring("tag_Mu7p5_MU", "dummy[pass=1,fail=0]"),
        tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25 = cms.vstring("tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25", "dummy[pass=1,fail=0]"),
        tag_Tight2012 = cms.vstring("tag_Tight2012", "dummy[pass=1,fail=0]"),
        # tag_Tight2016 = cms.vstring("tag_Tight2016", "dummy[pass=1,fail=0]"),
    ),


   #  Expressions = cms.PSet(
   #   Loose2015Var = cms.vstring("Loose2015Var", "PF==1", "PF"),
   #   Loose2016Var = cms.vstring("Loose2016Var", "Loose == 1", "Loose"), # Loose is present in TTrees! Doing it this way, in order to have a consistent definition of the IDs (cuts) below
   #   Medium2016Var = cms.vstring("Medium2016Var", "Loose == 1 && tkHitFract > 0.49 && ((Glb == 1 && glbChi2 < 3 && chi2LocPos < 12. && tkKink < 20. && segmentCompatibility > 3.03) || segmentCompatibility > 0.451)",
   #                               "Loose", "tkHitFract", "Glb", "glbChi2", "chi2LocPos", "tkKink", "segmentCompatibility"),
   #   Soft2016Var = cms.vstring("Soft2016Var", "TMOST == 1 && tkTrackerLay > 5 && tkPixelLay > 0 && abs(dzPV) < 20. && abs(dB) < 0.3",
   #                             "TMOST", "tkTrackerLay", "tkPixelLay", "dzPV", "dB"),
   #   Tight2016Var = cms.vstring("Tight2016Var", "Glb == 1 && PF == 1 && glbChi2 < 10 && glbValidMuHits > 0 && numberOfMatchedStations > 1 && dB < 0.2 && dzPV < 0.5 && tkValidPixelHits > 0 && tkTrackerLay > 5",
   #                              "Glb", "PF", "glbChi2", "glbValidMuHits", "numberOfMatchedStations", "dB", "dzPV", "tkValidPixelHits", "tkTrackerLay")
   # ),

   #  Cuts = cms.PSet(
   #        Loose2015 = cms.vstring("Loose2015", "Loose2015Var", "0.5"),
   #        Loose2016 = cms.vstring("Loose2016", "Loose2016Var", "0.5"),
   #        Medium2016 = cms.vstring("Medium2016", "Medium2016Var", "0.5"),
   #        Soft2016 = cms.vstring("Soft2016", "Soft2016Var", "0.5"),
   #        Tight2016 = cms.vstring("Tight2016", "Tight2016Var", "0.5"),
   #  ),


    Expressions = cms.PSet(
    ),

    Cuts = cms.PSet(
    ),

    PDFs = cms.PSet(
        signalPlusBkg = cms.vstring(
            "CBShape::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.06], alpha[3., 0.5, 5.], n[1, 0.1, 100.])",
            #"Chebychev::backgroundPass(mass, {cPass[0,-0.5,0.5], cPass2[0,-0.5,0.5]})",
            #"Chebychev::backgroundFail(mass, {cFail[0,-0.5,0.5], cFail2[0,-0.5,0.5]})",
            #"Gaussian::signal(mass, mean[3.1,3.0,3.2], sigma[0.05,0.02,0.1])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        # -- PDF Sets for the case of failing on error calculation by MINOS -- #
        vpvPlusExpo2 = cms.vstring(
            "Voigtian::signal1(mass, mean1[91,86,96], width[2.495], sigma1[2,1,5])",
            "Voigtian::signal2(mass, mean2[91,81,101], width,        sigma2[6,3,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        # -- Separate signal model of passing probe and failing probe -- #
        vpvPlusExpo3 = cms.vstring(
            "Voigtian::signalPass1(mass, meanPass1[91,84,98], width[2.495], sigmaPass1[2.5,1,6])",
            "Voigtian::signalPass2(mass, meanPass2[91,81,101], width,        sigmaPass2[5,1,10])",
            "SUM::signalPass(vFracPass[0.8,0,1]*signalPass1, signalPass2)",
            "Voigtian::signalFail1(mass, meanFail1[91,84,98], width[2.495], sigmaFail1[2.5,1,6])",
            "Voigtian::signalFail2(mass, meanFail2[91,81,101], width,        sigmaFail2[5,1,10])",
            "SUM::signalFail(vFracFail[0.8,0,1]*signalFail1, signalFail2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        # -- PDF Sets for the case of failing on error calculation by MINOS -- #
        vpvPlusExpo4 = cms.vstring(
            "Voigtian::signalPass1(mass, meanPass1[91,86,96], width[2.495], sigmaPass1[2.5,1,5])",
            "Voigtian::signalPass2(mass, meanPass2[91,78,104], width,        sigmaPass2[5,1,8])",
            "SUM::signalPass(vFracPass[0.7,0,1]*signalPass1, signalPass2)",
            "Voigtian::signalFail1(mass, meanFail1[91,86,96], width[2.495], sigmaFail1[2.5,1,5])",
            "Voigtian::signalFail2(mass, meanFail2[91,82,100], width,        sigmaFail2[5,1,10])",
            "SUM::signalFail(vFracFail[0.7,0,1]*signalFail1, signalFail2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),

        # -- PDF Sets for the case of failing on error calculation by MINOS -- #
        vpvPlusExpo5 = cms.vstring(
            "Voigtian::signalPass1(mass, meanPass1[91.1,86.3,96.1], width[2.495], sigmaPass1[2.52,1.4,5.1])",
            "Voigtian::signalPass2(mass, meanPass2[91.2,78.4,104.5], width,        sigmaPass2[5.12,1.3,8.2])",
            "SUM::signalPass(vFracPass[0.7,0,1]*signalPass1, signalPass2)",
            "Voigtian::signalFail1(mass, meanFail1[91.3,86.1,96.3], width[2.495], sigmaFail1[2.4,1,5.3])",
            "Voigtian::signalFail2(mass, meanFail2[91.2,82.5,100.5], width,        sigmaFail2[5.2,1,10.1])",
            "SUM::signalFail(vFracFail[0.7,0,1]*signalFail1, signalFail2)",
            "Exponential::backgroundPass(mass, lp[-0.11,-1.3,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.12,-1.2,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        
        vpvPlusExpoMin70 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        )
    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(False),

    Efficiencies = cms.PSet(), # will be filled later
)

Add_AdditionalBranches( PassingProbe, ProbeCondition )

# print Template.Categories

PtMin = 9999
List_Pt22 = ["IsoMu20_OR_IsoTkMu20", "IsoMu20", "IsoTkMu20", "L1_IsoMu20", "L2_IsoMu20", "L3_IsoMu20", "IsoF_IsoMu20", "TkMuF_IsoTkMu20", "IsoF_IsoTkMu20", "Tight2012", "RelTrkIso_010", "L3_IsoMu20_OR_TkMuF_IsoTkMu20"]
List_Pt24 = ["IsoMu22_OR_IsoTkMu22"]
List_Pt26 = ["IsoMu24_OR_IsoTkMu24", "IsoMu24", "IsoTkMu24", "L2_IsoMu24", "L3_IsoMu24", "IsoF_IsoMu24", "TkMuF_IsoTkMu24", "IsoF_IsoTkMu24", "L3_IsoMu24_OR_TkMuF_IsoTkMu24", "IsoF_IsoMu24_OR_IsoF_IsoTkMu24"]
List_Pt29 = ["IsoMu27", "IsoTkMu27", "IsoMu27_OR_IsoTkMu27"]
List_Pt47 = ["Mu45_eta2p1", "L1_Mu45_eta2p1", "L2_Mu45_eta2p1"]
List_Pt52 = ["Mu50", "HLT_TkMu50", "Mu50_OR_TkMu50", "L1_Mu50", "L2_Mu50"]
if PassingProbe in List_Pt22: PtMin = 22
elif PassingProbe in List_Pt24: PtMin = 24
elif PassingProbe in List_Pt26: PtMin = 26
elif PassingProbe in List_Pt29: PtMin = 29
elif PassingProbe in List_Pt47: PtMin = 47
elif PassingProbe in List_Pt52: PtMin = 52

EtaMax = 2.4
List_eta2p1 = ["Mu45_eta2p1", "L1_Mu45_eta2p1", "L2_Mu45_eta2p1"]
if PassingProbe in List_eta2p1: 
    EtaMax = 2.1

PT_ETA_BINS = cms.PSet(
                        pt     = cms.vdouble( 0, 9999 ), # -- Will be set later -- #
                        abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
                        # abseta = cms.vdouble(0.0, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),

                        # tag_IsoMu20 = cms.vstring("pass"),
                        # tag_pt =  cms.vdouble(22,9999)
                        # tag_IsoMu24 = cms.vstring("pass"),
                        tag_pt =  cms.vdouble(26,9999),
                        tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.2),
)

if PassingProbe in List_Pt22: PT_ETA_BINS.pt = cms.vdouble( 22, 25, 30, 40, 50, 60, 120, 200, 500 )
elif PassingProbe in List_Pt24: PT_ETA_BINS.pt = cms.vdouble( 24, 30, 40, 50, 60, 120, 200, 500 ) 
elif PassingProbe in List_Pt26: PT_ETA_BINS.pt = cms.vdouble( 26, 30, 40, 50, 60, 120, 200, 500 ) 
elif PassingProbe in List_Pt29: PT_ETA_BINS.pt = cms.vdouble( 29, 40, 50, 60, 120, 200, 500 ) 
elif PassingProbe in List_Pt47: PT_ETA_BINS.pt = cms.vdouble( 47, 50, 60, 120, 200, 500 )
elif PassingProbe in List_Pt52: PT_ETA_BINS.pt = cms.vdouble( 52, 55, 60, 80, 120, 200, 300, 400, 800 )
# elif PassingProbe in List_Pt52: PT_ETA_BINS.pt = cms.vdouble( 53, 100, 200, 700 )

if EtaMax == 2.1: PT_ETA_BINS.abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1)


PT_BINS = cms.PSet(
                        pt     = cms.vdouble( 0, 9999 ), #Will be set later
                        # abseta = cms.vdouble(0.0, EtaMax),
                        # abseta = cms.vdouble(0.0, 2.4),
                        # tag_IsoMu20 = cms.vstring("pass"),
                        # tag_pt = cms.vdouble(22,9999),
                        tag_IsoMu24 = cms.vstring("pass"),
                        # tag_Dimuon25_Jpsi = cms.vstring("pass"),
                        # tag_Mu50 = cms.vstring("pass"),
                        # tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q = cms.vstring("pass"),
                        # tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25 = cms.vstring("pass"),
                        # tag_IsoMu24XXX = cms.vstring("pass"),
                        # tag_Mu7p5_MU = cms.vstring("pass"),
                        # tag_Mu_L3 = cms.vstring("pass"),
                        tag_Tight2012 = cms.vstring("pass"),
                        tag_pt = cms.vdouble(26.0,9999.0),
                        # tag_abseta =  cms.vdouble(0, 2.4),
                        # pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                        # pair_drM1 = cms.vdouble(0.5,10),
                        # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.2),
                        # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.15),
                        # pt = cms.vdouble(26.0,9999.0),
)

PT_BINS.pt = cms.vdouble( 0, 5, 7, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 38, 42, 50, 60)
# PT_BINS.pt = cms.vdouble( 2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50, 60, 120, 200, 300, 500, 700, 1200 )
# PT_BINS.pt = cms.vdouble( 2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50, 60, 120, 200 )

# List_Binning_TurnOn_16 = ["L1SingleMu16"]
# List_Binning_TurnOn_18 = ["L1_IsoMu20"]
# List_Binning_TurnOn_20 = ["IsoMu20_OR_IsoTkMu20", "IsoMu20", "IsoTkMu20", "L2_IsoMu20", "L3_IsoMu20", "IsoF_IsoMu20", "TkMuF_IsoTkMu20", "IsoF_IsoTkMu20", "L2_Mu45_eta2p1", "L2_Mu50", "L3_IsoMu20_OR_TkMuF_IsoTkMu20"]
# List_Binning_TurnOn_22 = ["IsoMu22_OR_IsoTkMu22", "L1_Mu45_eta2p1", "L1_Mu50", "L1_IsoMu24"]
# List_Binning_TurnOn_24 = ["IsoMu24_OR_IsoTkMu24", "IsoMu24", "IsoTkMu24", "L2_IsoMu24", "L3_IsoMu24", "IsoF_IsoMu24", "TkMuF_IsoTkMu24", "IsoF_IsoTkMu24", "L3_IsoMu24_OR_TkMuF_IsoTkMu24", "IsoF_IsoMu24_OR_IsoF_IsoTkMu24"]
# List_Binning_TurnOn_26 = []
# List_Binning_TurnOn_27 = ["IsoMu27_OR_IsoTkMu27", "IsoMu27", "IsoTkMu27"]
# List_Binning_TurnOn_45 = ["Mu45_eta2p1"]
# List_Binning_TurnOn_50 = ["Mu50", "HLT_TkMu50", "Mu50_OR_TkMu50"]
# List_Binning_NoTurnOn = ["Tight2012", "RelTrkIso_010"]


# if PassingProbe in List_Binning_TurnOn_16:
#     PT_BINS.pt = cms.vdouble( 0, 10, 14, 16, 18, 20, 25, 30, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_18:
#     PT_BINS.pt = cms.vdouble( 0, 10, 16, 18, 20, 22, 25, 30, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_20:
#     PT_BINS.pt = cms.vdouble( 0, 10, 15, 18, 20, 22, 25, 30, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_22:
#     PT_BINS.pt = cms.vdouble( 0, 10, 15, 20, 22, 24, 26, 30, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_24:
#     PT_BINS.pt = cms.vdouble( 0, 10, 15, 18, 22, 24, 26, 30, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_26:
#     PT_BINS.pt = cms.vdouble( 0, 10, 15, 20, 24, 26, 28, 30, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_27:
#     PT_BINS.pt = cms.vdouble( 0, 15, 23, 25, 27, 29, 31, 40, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_45:
#     PT_BINS.pt = cms.vdouble( 0, 10, 15, 20, 25, 30, 40, 43, 45, 47, 50, 60, 80, 120, 200, 500 )
# elif PassingProbe in List_Binning_TurnOn_50:
#     PT_BINS.pt = cms.vdouble( 0, 10, 15, 20, 25, 30, 40, 45, 48, 50, 52, 55, 60, 80, 120, 200, 300, 400, 800 )
#     # PT_BINS.pt = cms.vdouble( 0, 10, 15, 20, 25, 30, 40, 45, 48, 50, 53, 100, 200, 700 )
# elif PassingProbe in List_Binning_NoTurnOn:
#     PT_BINS.pt = cms.vdouble( 22, 25, 30, 40, 50, 60, 80, 120, 200, 500 )

# PT_BINS.pt = cms.vdouble( 0, 10, 14, 16, 18, 20, 25, 30, 40, 50, 60, 80, 120, 200, 500 )
# PT_BINS.pt = cms.vdouble( 2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50, 60, 120, 200 )




DIMUON_PT_BINS = cms.PSet(
                        # pt     = cms.vdouble( 0, 9999 ), #Will be set later
                        pair_pt = cms.vdouble( 0, 9999 ), #Will be set later
 # abseta = cms.vdouble(0.0, EtaMax),
                        # abseta = cms.vdouble(0.0, 2.4),
                        # tag_IsoMu20 = cms.vstring("pass"),
                        # tag_pt = cms.vdouble(22,9999),
                        tag_IsoMu24 = cms.vstring("pass"),
                        # tag_Dimuon25_Jpsi = cms.vstring("pass"),
                        # tag_Mu50 = cms.vstring("pass"),
                        # tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q = cms.vstring("pass"),
                        # tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25 = cms.vstring("pass"),
                        # tag_IsoMu24XXX = cms.vstring("pass"),
                        # tag_Mu7p5_MU = cms.vstring("pass"),
                        # tag_Mu_L3 = cms.vstring("pass"),
                        tag_Tight2012 = cms.vstring("pass"),
                        tag_pt = cms.vdouble(26.0,9999.0),
                        # tag_abseta =  cms.vdouble(0, 2.4),
                        # pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                        # pair_drM1 = cms.vdouble(0.5,10),
                        # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.2),
                        # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.15),
                        # pt = cms.vdouble(26.0,9999.0),
)

DIMUON_PT_BINS.pair_pt = cms.vdouble( 0, 5, 7, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 38, 42, 50, 60, 120, 200, 300)
# DIMUON_PT_BINS.pair_pt = cms.vdouble( 2, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.5, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50, 60, 120, 200, 300, 500, 700, 1200 )



PtMin = 24.0
ETA_BINS = cms.PSet(
                    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
                    pt     = cms.vdouble( PtMin, 9999 ),
# abseta = cms.vdouble(0.0, EtaMax),
                        # abseta = cms.vdouble(0.0, 2.4),
                        # tag_IsoMu20 = cms.vstring("pass"),
                        # tag_pt = cms.vdouble(22,9999),
                        tag_IsoMu24 = cms.vstring("pass"),
                        # tag_Dimuon25_Jpsi = cms.vstring("pass"),
                        # tag_Mu50 = cms.vstring("pass"),
                        # tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q = cms.vstring("pass"),
                        # tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25 = cms.vstring("pass"),
                        # tag_IsoMu24XXX = cms.vstring("pass"),
                        # tag_Mu7p5_MU = cms.vstring("pass"),
                        # tag_Mu_L3 = cms.vstring("pass"),
                        tag_Tight2012 = cms.vstring("pass"),
                        tag_pt = cms.vdouble(26.0,9999.0),
                        # tag_abseta =  cms.vdouble(0, 2.4),
                        # pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                        # pair_drM1 = cms.vdouble(0.5,10),
                        # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.2),
                        # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.15),
                        # pt = cms.vdouble(26.0,9999.0),
                       )
if EtaMax == 2.1: ETA_BINS.eta = cms.vdouble(-2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1)

phi = 3.141592
degree15 = phi / 12;
EtaMax = 2.4
PHI_BINS = cms.PSet(
                    phi     = cms.vdouble( (-1)*degree15*12, (-1)*degree15*11, (-1)*degree15*9, (-1)*degree15*7, (-1)*degree15*5, (-1)*degree15*3, (-1)*degree15*1, degree15*1, degree15*3, degree15*5, degree15*7, degree15*9, degree15*11, degree15*12),
                    pt     = cms.vdouble( PtMin, 9999 ),
                    abseta = cms.vdouble(0.0, EtaMax),
                    # abseta = cms.vdouble(0.0, 2.4),
                    # tag_IsoMu20 = cms.vstring("pass"),
                    # tag_pt = cms.vdouble(22,9999),
                    tag_IsoMu24 = cms.vstring("pass"),
                    # tag_Dimuon25_Jpsi = cms.vstring("pass"),
                    # tag_Mu50 = cms.vstring("pass"),
                    # tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q = cms.vstring("pass"),
                    # tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25 = cms.vstring("pass"),
                    # tag_IsoMu24XXX = cms.vstring("pass"),
                    # tag_Mu7p5_MU = cms.vstring("pass"),
                    # tag_Mu_L3 = cms.vstring("pass"),
                    tag_Tight2012 = cms.vstring("pass"),
                    tag_pt = cms.vdouble(26.0,9999.0),
                    # tag_abseta =  cms.vdouble(0, 2.4),
                    # pair_probeMultiplicity = cms.vdouble(0.5,1.5),
                    # pair_drM1 = cms.vdouble(0.5,10),
                    # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.2),
                    # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.15),
                    # pt = cms.vdouble(26.0,9999.0),
                    )

VTX_BINS  = cms.PSet(
    tag_nVertices = cms.vdouble(2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 
                                22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5,
                                42.5, 44.5, 46.5, 48.5, 50.5),

    pt     = cms.vdouble(  PtMin, 9999 ),
    abseta = cms.vdouble(  0.0, EtaMax),
    # abseta = cms.vdouble(0.0, 2.4),
    # tag_IsoMu20 = cms.vstring("pass"),
    # tag_pt = cms.vdouble(22,9999),
    tag_IsoMu24 = cms.vstring("pass"),
    # tag_Dimuon25_Jpsi = cms.vstring("pass"),
    # tag_Mu50 = cms.vstring("pass"),
    # tag_hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q = cms.vstring("pass"),
    # tag_hltL3fL1sMu22orMu20erorMu25L1f0L2f0L3Filtered25 = cms.vstring("pass"),
    # tag_IsoMu24XXX = cms.vstring("pass"),
    # tag_Mu7p5_MU = cms.vstring("pass"),
    # tag_Mu_L3 = cms.vstring("pass"),
    tag_Tight2012 = cms.vstring("pass"),
    tag_pt = cms.vdouble(26.0,9999.0),
    # tag_abseta =  cms.vdouble(0, 2.4),
    # pair_probeMultiplicity = cms.vdouble(0.5,1.5),
    # pair_drM1 = cms.vdouble(0.5,10),
    # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.2),
    # tag_combRelIsoPF04dBeta =  cms.vdouble(0.0,0.15),
    # pt = cms.vdouble(26.0,9999.0),
)


process.TnP_MuonID = Template.clone(
    InputFileNames = cms.vstring(),
    InputTreeName = cms.string("fitter_tree"),
    InputDirectoryName = cms.string("tpTree"),
    # InputDirectoryName = cms.string("tpTreeOnePair"),
    OutputFileName = cms.string("TnP_MuonTrigger_%s.root" % scenario),
    Efficiencies = cms.PSet(),
)

#Add the variables for PU reweighting
if "_weight" in scenario:
    process.TnP_MuonID.WeightVariable = cms.string("weight")
    process.TnP_MuonID.Variables.weight = cms.vstring("weight","-10000","10000","")

if scenario=="data_25ns":
    process.TnP_MuonID.InputFileNames = Ntuple_Data

if "mc" in scenario:
    process.TnP_MuonID.InputFileNames = Ntuple_MC

#IDS = [ "IsoMu20","Mu20","L2fL1sMu16L1f0L2Filtered10Q","IsoTkMu20","L1sMu16"]
IDS = [args[1]] #here the id is taken from the arguments provided to cmsRun 
print IDS
# ALLBINS = [ ("pt",PT_BINS), ("eta",ETA_BINS), ("vtx",VTX_BINS), ("pteta",PT_ETA_BINS) ]
# ALLBINS = [ ("pt",PT_BINS), ("eta",ETA_BINS), ("phi",PHI_BINS), ("vtx",VTX_BINS), ("pteta",PT_ETA_BINS) ]
# ALLBINS = [ ("pt",PT_BINS), ("eta",ETA_BINS), ("vtx",VTX_BINS), ("InstLumi",InstLumi_BINS) ]
# ALLBINS = [ ("pt",PT_BINS), ("eta",ETA_BINS), ("phi",PHI_BINS), ("vtx",VTX_BINS) ]
# ALLBINS = [ ("eta",ETA_BINS) ]
# ALLBINS = [ ("eta",ETA_BINS), ("vtx",VTX_BINS) ]
# ALLBINS = [ ("vtx",VTX_BINS) ]
# ALLBINS = [ ("eta",ETA_BINS), ("vtx",VTX_BINS), ("phi",PHI_BINS) ]
# ALLBINS = [ ("pt",PT_BINS), ("eta",ETA_BINS), ("phi",PHI_BINS), ("vtx",VTX_BINS), ("pteta",PT_ETA_BINS) ]


ALLBINS = [ ("pt",PT_BINS), ("dimuon_pt",DIMUON_PT_BINS), ("eta",ETA_BINS), ("phi",PHI_BINS), ("vtx",VTX_BINS)]
# ALLBINS = [ ("pt",PT_BINS)]
# ALLBINS = [ ("dimuon_pt",DIMUON_PT_BINS)]


# ALLBINS = [ ("pteta",PT_ETA_BINS) ]
# ALLBINS = [("pteta",PT_ETA_BINS)]
# ALLBINS = [("run", RUN_BINS)]
# ALLBINS = [("pt",PT_BINS), ("eta",ETA_BINS), ("phi",PHI_BINS), ("InstLumi",InstLumi_BINS), ("bx",BX_BINS) ]
# ALLBINS = [("InstLumi",InstLumi_BINS)]

if len(args) > 1 and args[1] not in IDS: IDS += [ args[1] ]
for ID in IDS:
    print "now doing ",ID
    if len(args) > 1 and ID != args[1]: continue
    for X,B in ALLBINS:
        if len(args) > 2 and X not in args[2:]: continue
        #Add the information about ID and binning into the outputFileName
        module = process.TnP_MuonID.clone(OutputFileName = cms.string("TnP_MuonTrigger_%s_%s_%s.root" % (scenario, ID, X)))
        
        shape = "signalPlusBkg" #J/PSi
        # shape = "vpvPlusExpo3" #Z0
        
        # if X == "pteta": shape = "vpvPlusExpo3"
        # if X == "pteta": shape = "signalPlusBkg"

        #DEN: Binning
        DEN = B.clone(); num = ID; numstate = "pass"

        # -- dR condition between tag & probe muons for all binning (larger than 0.3) -- #
        # DEN.pair_deltaR = cms.vdouble(0.3, 999)

        # -- pair not critical: both on MC and data -- #
        # DEN.pair_dPhiPrimeDeg = cms.vdouble( 70, 9999 )            

        if "_from_" in ID:
            parts = ID.split("_from_")
            num = parts[0]
            # add Additional ID conditions to the binning ... 
            # ex> cmsRun TriggerEff.py mc IsoMu20_and_Tight2012_from_SIP4_and_PFIso25 => SIP4 and PFIso25 info. is added to the binning definition
            for D in parts[1].split("_and_"):
                if D == "dBeta_015": DEN.combRelIsoPF04dBeta = cms.vdouble(0, 0.15)
                elif D == "dBeta_025": DEN.combRelIsoPF04dBeta = cms.vdouble(0, 0.25)
                elif D == "RelTrkIso_010": DEN.relTkIso = cms.vdouble(0, 0.10)

                # Set D as the variable of DEN ... DEN.D = cms.vstring("pass")
                else: setattr(DEN, D, cms.vstring("pass"))

        print "#" * 100
        print "Binning variable: ", X
        print "Binning: ", DEN
        print "PDF: ", shape

        # numString: EfficiencyCategoryState variable. 
        # ex> cmsRun TriggerEff.py mc IsoMu20_and_Tight2012_from_SIP4_and_PFIso25 => numString = cms.vstring("IsoMu20", "pass", "Tight2012", "pass")
        numString = cms.vstring()
        for N in num.split("_and_"):
            numString += [N, "pass"]

        print "Passing probe condition: ", numString
        print "#" * 100
        print "\n"
        
        #Set Efficiency
        setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
            EfficiencyCategoryAndState = numString,
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = DEN,
            BinToPDFmap = cms.vstring(shape)
        ))

        if scenario.find("mc") != -1:
            # setattr(module.Efficiencies, ID+"_"+X+"_mcTrue", cms.PSet(
            #     EfficiencyCategoryAndState = numString,
            #     UnbinnedVariables = cms.vstring("mass"),
            #     BinnedVariables = DEN.clone(mcTrue = cms.vstring("true"))
            # ))
            if "_weight" in scenario:
                getattr(module.Efficiencies, ID+"_"+X).UnbinnedVariables.append("weight")
                # getattr(module.Efficiencies, ID+"_"+X+"_mcTrue").UnbinnedVariables.append("weight")

        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)     
        # print  process.TnP_MuonID   
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))

# print  process.TnP_MuonID   