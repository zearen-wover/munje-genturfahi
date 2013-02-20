from pyparsing import *
ParserElement.enablePackrat()

A_word_pre = Group(Literal(' CMAVO=(  A=( ')).setName('A_word_pre')
A_word_pre.resultsName = 'A_word_pre'
BAI_word_pre = Group(Literal(' CMAVO=(  BAI=( ')).setName('BAI_word_pre')
BAI_word_pre.resultsName = 'BAI_word_pre'
BAhE_word_pre = Group(Literal(' CMAVO=(  BAhE=( ')).setName('BAhE_word_pre')
BAhE_word_pre.resultsName = 'BAhE_word_pre'
BE_word_pre = Group(Literal(' CMAVO=(  BE=( ')).setName('BE_word_pre')
BE_word_pre.resultsName = 'BE_word_pre'
BEI_word_pre = Group(Literal(' CMAVO=(  BEI=( ')).setName('BEI_word_pre')
BEI_word_pre.resultsName = 'BEI_word_pre'
BEhO_word_pre = Group(Literal(' CMAVO=(  BEhO=( ')).setName('BEhO_word_pre')
BEhO_word_pre.resultsName = 'BEhO_word_pre'
BIhE_word_pre = Group(Literal(' CMAVO=(  BIhE=( ')).setName('BIhE_word_pre')
BIhE_word_pre.resultsName = 'BIhE_word_pre'
BIhI_word_pre = Group(Literal(' CMAVO=(  BIhI=( ')).setName('BIhI_word_pre')
BIhI_word_pre.resultsName = 'BIhI_word_pre'
BO_word_pre = Group(Literal(' CMAVO=(  BO=( ')).setName('BO_word_pre')
BO_word_pre.resultsName = 'BO_word_pre'
BOI_word_pre = Group(Literal(' CMAVO=(  BOI=( ')).setName('BOI_word_pre')
BOI_word_pre.resultsName = 'BOI_word_pre'
BRIVLA_word_pre = Group(Literal(' BRIVLA=( ')).setName('BRIVLA_word_pre')
BRIVLA_word_pre.resultsName = 'BRIVLA_word_pre'
BU_word_pre = Group(Literal(' CMAVO=(  BU=( ')).setName('BU_word_pre')
BU_word_pre.resultsName = 'BU_word_pre'
BY_word_pre = Group(Literal(' CMAVO=(  BY=( ')).setName('BY_word_pre')
BY_word_pre.resultsName = 'BY_word_pre'
CAI_word_pre = Group(Literal(' CMAVO=(  CAI=( ')).setName('CAI_word_pre')
CAI_word_pre.resultsName = 'CAI_word_pre'
CAhA_word_pre = Group(Literal(' CMAVO=(  CAhA=( ')).setName('CAhA_word_pre')
CAhA_word_pre.resultsName = 'CAhA_word_pre'
CEI_word_pre = Group(Literal(' CMAVO=(  CEI=( ')).setName('CEI_word_pre')
CEI_word_pre.resultsName = 'CEI_word_pre'
CEhE_word_pre = Group(Literal(' CMAVO=(  CEhE=( ')).setName('CEhE_word_pre')
CEhE_word_pre.resultsName = 'CEhE_word_pre'
CMAVO_word_pre = Group(Literal(' CMAVO=( ')).setName('CMAVO_word_pre')
CMAVO_word_pre.resultsName = 'CMAVO_word_pre'
CMENE_word_pre = Group(Literal(' CMENE=( ')).setName('CMENE_word_pre')
CMENE_word_pre.resultsName = 'CMENE_word_pre'
CO_word_pre = Group(Literal(' CMAVO=(  CO=( ')).setName('CO_word_pre')
CO_word_pre.resultsName = 'CO_word_pre'
COI_word_pre = Group(Literal(' CMAVO=(  COI=( ')).setName('COI_word_pre')
COI_word_pre.resultsName = 'COI_word_pre'
CU_word_pre = Group(Literal(' CMAVO=(  CU=( ')).setName('CU_word_pre')
CU_word_pre.resultsName = 'CU_word_pre'
CUhE_word_pre = Group(Literal(' CMAVO=(  CUhE=( ')).setName('CUhE_word_pre')
CUhE_word_pre.resultsName = 'CUhE_word_pre'
DAhO_word_pre = Group(Literal(' CMAVO=(  DAhO=( ')).setName('DAhO_word_pre')
DAhO_word_pre.resultsName = 'DAhO_word_pre'
DOI_word_pre = Group(Literal(' CMAVO=(  DOI=( ')).setName('DOI_word_pre')
DOI_word_pre.resultsName = 'DOI_word_pre'
DOhU_word_pre = Group(Literal(' CMAVO=(  DOhU=( ')).setName('DOhU_word_pre')
DOhU_word_pre.resultsName = 'DOhU_word_pre'
EOF = Group(StringEnd()).setName('EOF')
EOF.resultsName = 'EOF'
FA_word_pre = Group(Literal(' CMAVO=(  FA=( ')).setName('FA_word_pre')
FA_word_pre.resultsName = 'FA_word_pre'
FAhA_word_pre = Group(Literal(' CMAVO=(  FAhA=( ')).setName('FAhA_word_pre')
FAhA_word_pre.resultsName = 'FAhA_word_pre'
FAhO_word_pre = Group(Literal(' CMAVO=(  FAhO=( ')).setName('FAhO_word_pre')
FAhO_word_pre.resultsName = 'FAhO_word_pre'
FEhE_word_pre = Group(Literal(' CMAVO=(  FEhE=( ')).setName('FEhE_word_pre')
FEhE_word_pre.resultsName = 'FEhE_word_pre'
FEhU_word_pre = Group(Literal(' CMAVO=(  FEhU=( ')).setName('FEhU_word_pre')
FEhU_word_pre.resultsName = 'FEhU_word_pre'
FIhO_word_pre = Group(Literal(' CMAVO=(  FIhO=( ')).setName('FIhO_word_pre')
FIhO_word_pre.resultsName = 'FIhO_word_pre'
FOI_word_pre = Group(Literal(' CMAVO=(  FOI=( ')).setName('FOI_word_pre')
FOI_word_pre.resultsName = 'FOI_word_pre'
FUhA_word_pre = Group(Literal(' CMAVO=(  FUhA=( ')).setName('FUhA_word_pre')
FUhA_word_pre.resultsName = 'FUhA_word_pre'
FUhE_word_pre = Group(Literal(' CMAVO=(  FUhE=( ')).setName('FUhE_word_pre')
FUhE_word_pre.resultsName = 'FUhE_word_pre'
FUhO_word_pre = Group(Literal(' CMAVO=(  FUhO=( ')).setName('FUhO_word_pre')
FUhO_word_pre.resultsName = 'FUhO_word_pre'
GA_word_pre = Group(Literal(' CMAVO=(  GA=( ')).setName('GA_word_pre')
GA_word_pre.resultsName = 'GA_word_pre'
GAhO_word_pre = Group(Literal(' CMAVO=(  GAhO=( ')).setName('GAhO_word_pre')
GAhO_word_pre.resultsName = 'GAhO_word_pre'
GEhU_word_pre = Group(Literal(' CMAVO=(  GEhU=( ')).setName('GEhU_word_pre')
GEhU_word_pre.resultsName = 'GEhU_word_pre'
GI_word_pre = Group(Literal(' CMAVO=(  GI=( ')).setName('GI_word_pre')
GI_word_pre.resultsName = 'GI_word_pre'
GIhA_word_pre = Group(Literal(' CMAVO=(  GIhA=( ')).setName('GIhA_word_pre')
GIhA_word_pre.resultsName = 'GIhA_word_pre'
GOI_word_pre = Group(Literal(' CMAVO=(  GOI=( ')).setName('GOI_word_pre')
GOI_word_pre.resultsName = 'GOI_word_pre'
GOhA_word_pre = Group(Literal(' CMAVO=(  GOhA=( ')).setName('GOhA_word_pre')
GOhA_word_pre.resultsName = 'GOhA_word_pre'
GUhA_word_pre = Group(Literal(' CMAVO=(  GUhA=( ')).setName('GUhA_word_pre')
GUhA_word_pre.resultsName = 'GUhA_word_pre'
I_word_pre = Group(Literal(' CMAVO=(  I=( ')).setName('I_word_pre')
I_word_pre.resultsName = 'I_word_pre'
JA_word_pre = Group(Literal(' CMAVO=(  JA=( ')).setName('JA_word_pre')
JA_word_pre.resultsName = 'JA_word_pre'
JAI_word_pre = Group(Literal(' CMAVO=(  JAI=( ')).setName('JAI_word_pre')
JAI_word_pre.resultsName = 'JAI_word_pre'
JOI_word_pre = Group(Literal(' CMAVO=(  JOI=( ')).setName('JOI_word_pre')
JOI_word_pre.resultsName = 'JOI_word_pre'
JOhI_word_pre = Group(Literal(' CMAVO=(  JOhI=( ')).setName('JOhI_word_pre')
JOhI_word_pre.resultsName = 'JOhI_word_pre'
KE_word_pre = Group(Literal(' CMAVO=(  KE=( ')).setName('KE_word_pre')
KE_word_pre.resultsName = 'KE_word_pre'
KEI_word_pre = Group(Literal(' CMAVO=(  KEI=( ')).setName('KEI_word_pre')
KEI_word_pre.resultsName = 'KEI_word_pre'
KEhE_word_pre = Group(Literal(' CMAVO=(  KEhE=( ')).setName('KEhE_word_pre')
KEhE_word_pre.resultsName = 'KEhE_word_pre'
KI_word_pre = Group(Literal(' CMAVO=(  KI=( ')).setName('KI_word_pre')
KI_word_pre.resultsName = 'KI_word_pre'
KOhA_word_pre = Group(Literal(' CMAVO=(  KOhA=( ')).setName('KOhA_word_pre')
KOhA_word_pre.resultsName = 'KOhA_word_pre'
KU_word_pre = Group(Literal(' CMAVO=(  KU=( ')).setName('KU_word_pre')
KU_word_pre.resultsName = 'KU_word_pre'
KUhE_word_pre = Group(Literal(' CMAVO=(  KUhE=( ')).setName('KUhE_word_pre')
KUhE_word_pre.resultsName = 'KUhE_word_pre'
KUhO_word_pre = Group(Literal(' CMAVO=(  KUhO=( ')).setName('KUhO_word_pre')
KUhO_word_pre.resultsName = 'KUhO_word_pre'
LA_word_pre = Group(Literal(' CMAVO=(  LA=( ')).setName('LA_word_pre')
LA_word_pre.resultsName = 'LA_word_pre'
LAU_word_pre = Group(Literal(' CMAVO=(  LAU=( ')).setName('LAU_word_pre')
LAU_word_pre.resultsName = 'LAU_word_pre'
LAhE_word_pre = Group(Literal(' CMAVO=(  LAhE=( ')).setName('LAhE_word_pre')
LAhE_word_pre.resultsName = 'LAhE_word_pre'
LE_word_pre = Group(Literal(' CMAVO=(  LE=( ')).setName('LE_word_pre')
LE_word_pre.resultsName = 'LE_word_pre'
LEhU_word_pre = Group(Literal(' CMAVO=(  LEhU=( ')).setName('LEhU_word_pre')
LEhU_word_pre.resultsName = 'LEhU_word_pre'
LI_word_pre = Group(Literal(' CMAVO=(  LI=( ')).setName('LI_word_pre')
LI_word_pre.resultsName = 'LI_word_pre'
LIhU_word_pre = Group(Literal(' CMAVO=(  LIhU=( ')).setName('LIhU_word_pre')
LIhU_word_pre.resultsName = 'LIhU_word_pre'
LOhO_word_pre = Group(Literal(' CMAVO=(  LOhO=( ')).setName('LOhO_word_pre')
LOhO_word_pre.resultsName = 'LOhO_word_pre'
LOhU_word_pre = Group(Literal(' CMAVO=(  LOhU=( ')).setName('LOhU_word_pre')
LOhU_word_pre.resultsName = 'LOhU_word_pre'
LU_word_pre = Group(Literal(' CMAVO=(  LU=( ')).setName('LU_word_pre')
LU_word_pre.resultsName = 'LU_word_pre'
LUhU_word_pre = Group(Literal(' CMAVO=(  LUhU=( ')).setName('LUhU_word_pre')
LUhU_word_pre.resultsName = 'LUhU_word_pre'
MAI_word_pre = Group(Literal(' CMAVO=(  MAI=( ')).setName('MAI_word_pre')
MAI_word_pre.resultsName = 'MAI_word_pre'
MAhO_word_pre = Group(Literal(' CMAVO=(  MAhO=( ')).setName('MAhO_word_pre')
MAhO_word_pre.resultsName = 'MAhO_word_pre'
ME_word_pre = Group(Literal(' CMAVO=(  ME=( ')).setName('ME_word_pre')
ME_word_pre.resultsName = 'ME_word_pre'
MEhU_word_pre = Group(Literal(' CMAVO=(  MEhU=( ')).setName('MEhU_word_pre')
MEhU_word_pre.resultsName = 'MEhU_word_pre'
MOI_word_pre = Group(Literal(' CMAVO=(  MOI=( ')).setName('MOI_word_pre')
MOI_word_pre.resultsName = 'MOI_word_pre'
MOhE_word_pre = Group(Literal(' CMAVO=(  MOhE=( ')).setName('MOhE_word_pre')
MOhE_word_pre.resultsName = 'MOhE_word_pre'
MOhI_word_pre = Group(Literal(' CMAVO=(  MOhI=( ')).setName('MOhI_word_pre')
MOhI_word_pre.resultsName = 'MOhI_word_pre'
NA_word_pre = Group(Literal(' CMAVO=(  NA=( ')).setName('NA_word_pre')
NA_word_pre.resultsName = 'NA_word_pre'
NAI_word_pre = Group(Literal(' CMAVO=(  NAI=( ')).setName('NAI_word_pre')
NAI_word_pre.resultsName = 'NAI_word_pre'
NAhE_word_pre = Group(Literal(' CMAVO=(  NAhE=( ')).setName('NAhE_word_pre')
NAhE_word_pre.resultsName = 'NAhE_word_pre'
NAhU_word_pre = Group(Literal(' CMAVO=(  NAhU=( ')).setName('NAhU_word_pre')
NAhU_word_pre.resultsName = 'NAhU_word_pre'
NIhE_word_pre = Group(Literal(' CMAVO=(  NIhE=( ')).setName('NIhE_word_pre')
NIhE_word_pre.resultsName = 'NIhE_word_pre'
NIhO_word_pre = Group(Literal(' CMAVO=(  NIhO=( ')).setName('NIhO_word_pre')
NIhO_word_pre.resultsName = 'NIhO_word_pre'
NOI_word_pre = Group(Literal(' CMAVO=(  NOI=( ')).setName('NOI_word_pre')
NOI_word_pre.resultsName = 'NOI_word_pre'
NU_word_pre = Group(Literal(' CMAVO=(  NU=( ')).setName('NU_word_pre')
NU_word_pre.resultsName = 'NU_word_pre'
NUhA_word_pre = Group(Literal(' CMAVO=(  NUhA=( ')).setName('NUhA_word_pre')
NUhA_word_pre.resultsName = 'NUhA_word_pre'
NUhI_word_pre = Group(Literal(' CMAVO=(  NUhI=( ')).setName('NUhI_word_pre')
NUhI_word_pre.resultsName = 'NUhI_word_pre'
NUhU_word_pre = Group(Literal(' CMAVO=(  NUhU=( ')).setName('NUhU_word_pre')
NUhU_word_pre.resultsName = 'NUhU_word_pre'
PA_word_pre = Group(Literal(' CMAVO=(  PA=( ')).setName('PA_word_pre')
PA_word_pre.resultsName = 'PA_word_pre'
PEhE_word_pre = Group(Literal(' CMAVO=(  PEhE=( ')).setName('PEhE_word_pre')
PEhE_word_pre.resultsName = 'PEhE_word_pre'
PEhO_word_pre = Group(Literal(' CMAVO=(  PEhO=( ')).setName('PEhO_word_pre')
PEhO_word_pre.resultsName = 'PEhO_word_pre'
PU_word_pre = Group(Literal(' CMAVO=(  PU=( ')).setName('PU_word_pre')
PU_word_pre.resultsName = 'PU_word_pre'
RAhO_word_pre = Group(Literal(' CMAVO=(  RAhO=( ')).setName('RAhO_word_pre')
RAhO_word_pre.resultsName = 'RAhO_word_pre'
ROI_word_pre = Group(Literal(' CMAVO=(  ROI=( ')).setName('ROI_word_pre')
ROI_word_pre.resultsName = 'ROI_word_pre'
SA_word_pre = Group(Literal(' CMAVO=(  SA=( ')).setName('SA_word_pre')
SA_word_pre.resultsName = 'SA_word_pre'
SE_word_pre = Group(Literal(' CMAVO=(  SE=( ')).setName('SE_word_pre')
SE_word_pre.resultsName = 'SE_word_pre'
SEI_word_pre = Group(Literal(' CMAVO=(  SEI=( ')).setName('SEI_word_pre')
SEI_word_pre.resultsName = 'SEI_word_pre'
SEhU_word_pre = Group(Literal(' CMAVO=(  SEhU=( ')).setName('SEhU_word_pre')
SEhU_word_pre.resultsName = 'SEhU_word_pre'
SI_word_pre = Group(Literal(' CMAVO=(  SI=( ')).setName('SI_word_pre')
SI_word_pre.resultsName = 'SI_word_pre'
SOI_word_pre = Group(Literal(' CMAVO=(  SOI=( ')).setName('SOI_word_pre')
SOI_word_pre.resultsName = 'SOI_word_pre'
SU_word_pre = Group(Literal(' CMAVO=(  SU=( ')).setName('SU_word_pre')
SU_word_pre.resultsName = 'SU_word_pre'
TAhE_word_pre = Group(Literal(' CMAVO=(  TAhE=( ')).setName('TAhE_word_pre')
TAhE_word_pre.resultsName = 'TAhE_word_pre'
TEI_word_pre = Group(Literal(' CMAVO=(  TEI=( ')).setName('TEI_word_pre')
TEI_word_pre.resultsName = 'TEI_word_pre'
TEhU_word_pre = Group(Literal(' CMAVO=(  TEhU=( ')).setName('TEhU_word_pre')
TEhU_word_pre.resultsName = 'TEhU_word_pre'
TO_word_pre = Group(Literal(' CMAVO=(  TO=( ')).setName('TO_word_pre')
TO_word_pre.resultsName = 'TO_word_pre'
TOI_word_pre = Group(Literal(' CMAVO=(  TOI=( ')).setName('TOI_word_pre')
TOI_word_pre.resultsName = 'TOI_word_pre'
TUhE_word_pre = Group(Literal(' CMAVO=(  TUhE=( ')).setName('TUhE_word_pre')
TUhE_word_pre.resultsName = 'TUhE_word_pre'
TUhU_word_pre = Group(Literal(' CMAVO=(  TUhU=( ')).setName('TUhU_word_pre')
TUhU_word_pre.resultsName = 'TUhU_word_pre'
UI_word_pre = Group(Literal(' CMAVO=(  UI=( ')).setName('UI_word_pre')
UI_word_pre.resultsName = 'UI_word_pre'
VA_word_pre = Group(Literal(' CMAVO=(  VA=( ')).setName('VA_word_pre')
VA_word_pre.resultsName = 'VA_word_pre'
VAU_word_pre = Group(Literal(' CMAVO=(  VAU=( ')).setName('VAU_word_pre')
VAU_word_pre.resultsName = 'VAU_word_pre'
VEI_word_pre = Group(Literal(' CMAVO=(  VEI=( ')).setName('VEI_word_pre')
VEI_word_pre.resultsName = 'VEI_word_pre'
VEhA_word_pre = Group(Literal(' CMAVO=(  VEhA=( ')).setName('VEhA_word_pre')
VEhA_word_pre.resultsName = 'VEhA_word_pre'
VEhO_word_pre = Group(Literal(' CMAVO=(  VEhO=( ')).setName('VEhO_word_pre')
VEhO_word_pre.resultsName = 'VEhO_word_pre'
VIhA_word_pre = Group(Literal(' CMAVO=(  VIhA=( ')).setName('VIhA_word_pre')
VIhA_word_pre.resultsName = 'VIhA_word_pre'
VUhO_word_pre = Group(Literal(' CMAVO=(  VUhO=( ')).setName('VUhO_word_pre')
VUhO_word_pre.resultsName = 'VUhO_word_pre'
VUhU_word_pre = Group(Literal(' CMAVO=(  VUhU=( ')).setName('VUhU_word_pre')
VUhU_word_pre.resultsName = 'VUhU_word_pre'
XI_word_pre = Group(Literal(' CMAVO=(  XI=( ')).setName('XI_word_pre')
XI_word_pre.resultsName = 'XI_word_pre'
ZAhO_word_pre = Group(Literal(' CMAVO=(  ZAhO=( ')).setName('ZAhO_word_pre')
ZAhO_word_pre.resultsName = 'ZAhO_word_pre'
ZEI_word_pre = Group(Literal(' CMAVO=(  ZEI=( ')).setName('ZEI_word_pre')
ZEI_word_pre.resultsName = 'ZEI_word_pre'
ZEhA_word_pre = Group(Literal(' CMAVO=(  ZEhA=( ')).setName('ZEhA_word_pre')
ZEhA_word_pre.resultsName = 'ZEhA_word_pre'
ZI_word_pre = Group(Literal(' CMAVO=(  ZI=( ')).setName('ZI_word_pre')
ZI_word_pre.resultsName = 'ZI_word_pre'
ZIhE_word_pre = Group(Literal(' CMAVO=(  ZIhE=( ')).setName('ZIhE_word_pre')
ZIhE_word_pre.resultsName = 'ZIhE_word_pre'
ZO_word_pre = Group(Literal(' CMAVO=(  ZO=( ')).setName('ZO_word_pre')
ZO_word_pre.resultsName = 'ZO_word_pre'
ZOI_word_pre = Group(Literal(' CMAVO=(  ZOI=( ')).setName('ZOI_word_pre')
ZOI_word_pre.resultsName = 'ZOI_word_pre'
ZOhU_word_pre = Group(Literal(' CMAVO=(  ZOhU=( ')).setName('ZOhU_word_pre')
ZOhU_word_pre.resultsName = 'ZOhU_word_pre'
close_paren = Group(Literal(' ) ')).setName('close_paren')
close_paren.resultsName = 'close_paren'
close_paren_char = Group(Literal(')')).setName('close_paren_char')
close_paren_char.resultsName = 'close_paren_char'
dot_star = Group(Empty()).setName('dot_star')
dot_star.resultsName = 'dot_star'
equals_char = Group(Literal('=')).setName('equals_char')
equals_char.resultsName = 'equals_char'
non_Lojban_word_pre = Group(Literal(' nonLojbanWord=( ')).setName('non_Lojban_word_pre')
non_Lojban_word_pre.resultsName = 'non_Lojban_word_pre'
open_paren = Group(Literal('( ')).setName('open_paren')
open_paren.resultsName = 'open_paren'
space_char = Group(Literal(' ')).setName('space_char')
space_char.resultsName = 'space_char'
spaces_pre = Group(Literal(' spaces=( ') | Literal(' initialSpaces=( ')).setName('spaces_pre')
spaces_pre.resultsName = 'spaces_pre'
zoi_close = Group(Literal('Im hard coded and not context free !')).setName('zoi_close')
zoi_close.resultsName = 'zoi_close'
zoi_open = Group(Literal('Im hard coded and not context free !')).setName('zoi_open')
zoi_open.resultsName = 'zoi_open'
zoi_word = Group(Literal('Im hard coded and not context free !')).setName('zoi_word')
zoi_word.resultsName = 'zoi_word'
any_word_pre = Group(CMAVO_word_pre | CMENE_word_pre | BRIVLA_word_pre).setName('any_word_pre')
any_word_pre.resultsName = 'any_word_pre'
known_cmavo_pre = Group(A_word_pre | BAI_word_pre | BAhE_word_pre | BE_word_pre | BEI_word_pre | BEhO_word_pre | BIhE_word_pre | BIhI_word_pre | BO_word_pre | BOI_word_pre | BU_word_pre | BY_word_pre | CAI_word_pre | CAhA_word_pre | CEI_word_pre | CEhE_word_pre | CO_word_pre | COI_word_pre | CU_word_pre | CUhE_word_pre | DAhO_word_pre | DOI_word_pre | DOhU_word_pre | FA_word_pre | FAhA_word_pre | FAhO_word_pre | FEhE_word_pre | FEhU_word_pre | FIhO_word_pre | FOI_word_pre | FUhA_word_pre | FUhE_word_pre | FUhO_word_pre | GA_word_pre | GAhO_word_pre | GEhU_word_pre | GI_word_pre | GIhA_word_pre | GOI_word_pre | GOhA_word_pre | GUhA_word_pre | I_word_pre | JA_word_pre | JAI_word_pre | JOI_word_pre | JOhI_word_pre | KE_word_pre | KEI_word_pre | KEhE_word_pre | KI_word_pre | KOhA_word_pre | KU_word_pre | KUhE_word_pre | KUhO_word_pre | LA_word_pre | LAU_word_pre | LAhE_word_pre | LE_word_pre | LEhU_word_pre | LI_word_pre | LIhU_word_pre | LOhO_word_pre | LOhU_word_pre | LU_word_pre | LUhU_word_pre | MAI_word_pre | MAhO_word_pre | ME_word_pre | MEhU_word_pre | MOI_word_pre | MOhE_word_pre | MOhI_word_pre | NA_word_pre | NAI_word_pre | NAhE_word_pre | NAhU_word_pre | NIhE_word_pre | NIhO_word_pre | NOI_word_pre | NU_word_pre | NUhA_word_pre | NUhI_word_pre | NUhU_word_pre | PA_word_pre | PEhE_word_pre | PEhO_word_pre | PU_word_pre | RAhO_word_pre | ROI_word_pre | SA_word_pre | SE_word_pre | SEI_word_pre | SEhU_word_pre | SI_word_pre | SOI_word_pre | SU_word_pre | TAhE_word_pre | TEI_word_pre | TEhU_word_pre | TO_word_pre | TOI_word_pre | TUhE_word_pre | TUhU_word_pre | UI_word_pre | VA_word_pre | VAU_word_pre | VEI_word_pre | VEhA_word_pre | VEhO_word_pre | VIhA_word_pre | VUhO_word_pre | VUhU_word_pre | XI_word_pre | ZAhO_word_pre | ZEI_word_pre | ZEhA_word_pre | ZI_word_pre | ZIhE_word_pre | ZO_word_pre | ZOI_word_pre | ZOhU_word_pre).setName('known_cmavo_pre')
known_cmavo_pre.resultsName = 'known_cmavo_pre'
zoi_printable_pre = Group(any_word_pre | non_Lojban_word_pre).setName('zoi_printable_pre')
zoi_printable_pre.resultsName = 'zoi_printable_pre'

A = Forward().setName('A')
A.resultsName = 'A'
A_clause = Forward().setName('A_clause')
A_clause.resultsName = 'A_clause'
A_post = Forward().setName('A_post')
A_post.resultsName = 'A_post'
A_pre = Forward().setName('A_pre')
A_pre.resultsName = 'A_pre'
BAI = Forward().setName('BAI')
BAI.resultsName = 'BAI'
BAI_clause = Forward().setName('BAI_clause')
BAI_clause.resultsName = 'BAI_clause'
BAI_post = Forward().setName('BAI_post')
BAI_post.resultsName = 'BAI_post'
BAI_pre = Forward().setName('BAI_pre')
BAI_pre.resultsName = 'BAI_pre'
BAhE = Forward().setName('BAhE')
BAhE.resultsName = 'BAhE'
BAhE_clause = Forward().setName('BAhE_clause')
BAhE_clause.resultsName = 'BAhE_clause'
BAhE_post = Forward().setName('BAhE_post')
BAhE_post.resultsName = 'BAhE_post'
BAhE_pre = Forward().setName('BAhE_pre')
BAhE_pre.resultsName = 'BAhE_pre'
BE = Forward().setName('BE')
BE.resultsName = 'BE'
BE_clause = Forward().setName('BE_clause')
BE_clause.resultsName = 'BE_clause'
BE_post = Forward().setName('BE_post')
BE_post.resultsName = 'BE_post'
BE_pre = Forward().setName('BE_pre')
BE_pre.resultsName = 'BE_pre'
BEI = Forward().setName('BEI')
BEI.resultsName = 'BEI'
BEI_clause = Forward().setName('BEI_clause')
BEI_clause.resultsName = 'BEI_clause'
BEI_post = Forward().setName('BEI_post')
BEI_post.resultsName = 'BEI_post'
BEI_pre = Forward().setName('BEI_pre')
BEI_pre.resultsName = 'BEI_pre'
BEhO = Forward().setName('BEhO')
BEhO.resultsName = 'BEhO'
BEhO_clause = Forward().setName('BEhO_clause')
BEhO_clause.resultsName = 'BEhO_clause'
BEhO_post = Forward().setName('BEhO_post')
BEhO_post.resultsName = 'BEhO_post'
BEhO_pre = Forward().setName('BEhO_pre')
BEhO_pre.resultsName = 'BEhO_pre'
BIhE = Forward().setName('BIhE')
BIhE.resultsName = 'BIhE'
BIhE_clause = Forward().setName('BIhE_clause')
BIhE_clause.resultsName = 'BIhE_clause'
BIhE_post = Forward().setName('BIhE_post')
BIhE_post.resultsName = 'BIhE_post'
BIhE_pre = Forward().setName('BIhE_pre')
BIhE_pre.resultsName = 'BIhE_pre'
BIhI = Forward().setName('BIhI')
BIhI.resultsName = 'BIhI'
BIhI_clause = Forward().setName('BIhI_clause')
BIhI_clause.resultsName = 'BIhI_clause'
BIhI_post = Forward().setName('BIhI_post')
BIhI_post.resultsName = 'BIhI_post'
BIhI_pre = Forward().setName('BIhI_pre')
BIhI_pre.resultsName = 'BIhI_pre'
BO = Forward().setName('BO')
BO.resultsName = 'BO'
BO_clause = Forward().setName('BO_clause')
BO_clause.resultsName = 'BO_clause'
BO_post = Forward().setName('BO_post')
BO_post.resultsName = 'BO_post'
BO_pre = Forward().setName('BO_pre')
BO_pre.resultsName = 'BO_pre'
BOI = Forward().setName('BOI')
BOI.resultsName = 'BOI'
BOI_clause = Forward().setName('BOI_clause')
BOI_clause.resultsName = 'BOI_clause'
BOI_post = Forward().setName('BOI_post')
BOI_post.resultsName = 'BOI_post'
BOI_pre = Forward().setName('BOI_pre')
BOI_pre.resultsName = 'BOI_pre'
BRIVLA = Forward().setName('BRIVLA')
BRIVLA.resultsName = 'BRIVLA'
BRIVLA_clause = Forward().setName('BRIVLA_clause')
BRIVLA_clause.resultsName = 'BRIVLA_clause'
BRIVLA_post = Forward().setName('BRIVLA_post')
BRIVLA_post.resultsName = 'BRIVLA_post'
BRIVLA_pre = Forward().setName('BRIVLA_pre')
BRIVLA_pre.resultsName = 'BRIVLA_pre'
BU = Forward().setName('BU')
BU.resultsName = 'BU'
BU_clause = Forward().setName('BU_clause')
BU_clause.resultsName = 'BU_clause'
BU_post = Forward().setName('BU_post')
BU_post.resultsName = 'BU_post'
BU_pre = Forward().setName('BU_pre')
BU_pre.resultsName = 'BU_pre'
BY = Forward().setName('BY')
BY.resultsName = 'BY'
BY_clause = Forward().setName('BY_clause')
BY_clause.resultsName = 'BY_clause'
BY_post = Forward().setName('BY_post')
BY_post.resultsName = 'BY_post'
BY_pre = Forward().setName('BY_pre')
BY_pre.resultsName = 'BY_pre'
CAI = Forward().setName('CAI')
CAI.resultsName = 'CAI'
CAI_clause = Forward().setName('CAI_clause')
CAI_clause.resultsName = 'CAI_clause'
CAI_post = Forward().setName('CAI_post')
CAI_post.resultsName = 'CAI_post'
CAI_pre = Forward().setName('CAI_pre')
CAI_pre.resultsName = 'CAI_pre'
CAhA = Forward().setName('CAhA')
CAhA.resultsName = 'CAhA'
CAhA_clause = Forward().setName('CAhA_clause')
CAhA_clause.resultsName = 'CAhA_clause'
CAhA_post = Forward().setName('CAhA_post')
CAhA_post.resultsName = 'CAhA_post'
CAhA_pre = Forward().setName('CAhA_pre')
CAhA_pre.resultsName = 'CAhA_pre'
CEI = Forward().setName('CEI')
CEI.resultsName = 'CEI'
CEI_clause = Forward().setName('CEI_clause')
CEI_clause.resultsName = 'CEI_clause'
CEI_post = Forward().setName('CEI_post')
CEI_post.resultsName = 'CEI_post'
CEI_pre = Forward().setName('CEI_pre')
CEI_pre.resultsName = 'CEI_pre'
CEhE = Forward().setName('CEhE')
CEhE.resultsName = 'CEhE'
CEhE_clause = Forward().setName('CEhE_clause')
CEhE_clause.resultsName = 'CEhE_clause'
CEhE_post = Forward().setName('CEhE_post')
CEhE_post.resultsName = 'CEhE_post'
CEhE_pre = Forward().setName('CEhE_pre')
CEhE_pre.resultsName = 'CEhE_pre'
CMAVO = Forward().setName('CMAVO')
CMAVO.resultsName = 'CMAVO'
CMAVO_pre = Forward().setName('CMAVO_pre')
CMAVO_pre.resultsName = 'CMAVO_pre'
CMENE = Forward().setName('CMENE')
CMENE.resultsName = 'CMENE'
CMENE_clause = Forward().setName('CMENE_clause')
CMENE_clause.resultsName = 'CMENE_clause'
CMENE_post = Forward().setName('CMENE_post')
CMENE_post.resultsName = 'CMENE_post'
CMENE_pre = Forward().setName('CMENE_pre')
CMENE_pre.resultsName = 'CMENE_pre'
CO = Forward().setName('CO')
CO.resultsName = 'CO'
CO_clause = Forward().setName('CO_clause')
CO_clause.resultsName = 'CO_clause'
CO_post = Forward().setName('CO_post')
CO_post.resultsName = 'CO_post'
CO_pre = Forward().setName('CO_pre')
CO_pre.resultsName = 'CO_pre'
COI = Forward().setName('COI')
COI.resultsName = 'COI'
COI_clause = Forward().setName('COI_clause')
COI_clause.resultsName = 'COI_clause'
COI_post = Forward().setName('COI_post')
COI_post.resultsName = 'COI_post'
COI_pre = Forward().setName('COI_pre')
COI_pre.resultsName = 'COI_pre'
CU = Forward().setName('CU')
CU.resultsName = 'CU'
CU_clause = Forward().setName('CU_clause')
CU_clause.resultsName = 'CU_clause'
CU_post = Forward().setName('CU_post')
CU_post.resultsName = 'CU_post'
CU_pre = Forward().setName('CU_pre')
CU_pre.resultsName = 'CU_pre'
CUhE = Forward().setName('CUhE')
CUhE.resultsName = 'CUhE'
CUhE_clause = Forward().setName('CUhE_clause')
CUhE_clause.resultsName = 'CUhE_clause'
CUhE_post = Forward().setName('CUhE_post')
CUhE_post.resultsName = 'CUhE_post'
CUhE_pre = Forward().setName('CUhE_pre')
CUhE_pre.resultsName = 'CUhE_pre'
DAhO = Forward().setName('DAhO')
DAhO.resultsName = 'DAhO'
DAhO_clause = Forward().setName('DAhO_clause')
DAhO_clause.resultsName = 'DAhO_clause'
DAhO_post = Forward().setName('DAhO_post')
DAhO_post.resultsName = 'DAhO_post'
DAhO_pre = Forward().setName('DAhO_pre')
DAhO_pre.resultsName = 'DAhO_pre'
DOI = Forward().setName('DOI')
DOI.resultsName = 'DOI'
DOI_clause = Forward().setName('DOI_clause')
DOI_clause.resultsName = 'DOI_clause'
DOI_post = Forward().setName('DOI_post')
DOI_post.resultsName = 'DOI_post'
DOI_pre = Forward().setName('DOI_pre')
DOI_pre.resultsName = 'DOI_pre'
DOhU = Forward().setName('DOhU')
DOhU.resultsName = 'DOhU'
DOhU_clause = Forward().setName('DOhU_clause')
DOhU_clause.resultsName = 'DOhU_clause'
DOhU_post = Forward().setName('DOhU_post')
DOhU_post.resultsName = 'DOhU_post'
DOhU_pre = Forward().setName('DOhU_pre')
DOhU_pre.resultsName = 'DOhU_pre'
FA = Forward().setName('FA')
FA.resultsName = 'FA'
FA_clause = Forward().setName('FA_clause')
FA_clause.resultsName = 'FA_clause'
FA_post = Forward().setName('FA_post')
FA_post.resultsName = 'FA_post'
FA_pre = Forward().setName('FA_pre')
FA_pre.resultsName = 'FA_pre'
FAhA = Forward().setName('FAhA')
FAhA.resultsName = 'FAhA'
FAhA_clause = Forward().setName('FAhA_clause')
FAhA_clause.resultsName = 'FAhA_clause'
FAhA_post = Forward().setName('FAhA_post')
FAhA_post.resultsName = 'FAhA_post'
FAhA_pre = Forward().setName('FAhA_pre')
FAhA_pre.resultsName = 'FAhA_pre'
FAhO = Forward().setName('FAhO')
FAhO.resultsName = 'FAhO'
FAhO_clause = Forward().setName('FAhO_clause')
FAhO_clause.resultsName = 'FAhO_clause'
FEhE = Forward().setName('FEhE')
FEhE.resultsName = 'FEhE'
FEhE_clause = Forward().setName('FEhE_clause')
FEhE_clause.resultsName = 'FEhE_clause'
FEhE_post = Forward().setName('FEhE_post')
FEhE_post.resultsName = 'FEhE_post'
FEhE_pre = Forward().setName('FEhE_pre')
FEhE_pre.resultsName = 'FEhE_pre'
FEhU = Forward().setName('FEhU')
FEhU.resultsName = 'FEhU'
FEhU_clause = Forward().setName('FEhU_clause')
FEhU_clause.resultsName = 'FEhU_clause'
FEhU_post = Forward().setName('FEhU_post')
FEhU_post.resultsName = 'FEhU_post'
FEhU_pre = Forward().setName('FEhU_pre')
FEhU_pre.resultsName = 'FEhU_pre'
FIhO = Forward().setName('FIhO')
FIhO.resultsName = 'FIhO'
FIhO_clause = Forward().setName('FIhO_clause')
FIhO_clause.resultsName = 'FIhO_clause'
FIhO_post = Forward().setName('FIhO_post')
FIhO_post.resultsName = 'FIhO_post'
FIhO_pre = Forward().setName('FIhO_pre')
FIhO_pre.resultsName = 'FIhO_pre'
FOI = Forward().setName('FOI')
FOI.resultsName = 'FOI'
FOI_clause = Forward().setName('FOI_clause')
FOI_clause.resultsName = 'FOI_clause'
FOI_post = Forward().setName('FOI_post')
FOI_post.resultsName = 'FOI_post'
FOI_pre = Forward().setName('FOI_pre')
FOI_pre.resultsName = 'FOI_pre'
FUhA = Forward().setName('FUhA')
FUhA.resultsName = 'FUhA'
FUhA_clause = Forward().setName('FUhA_clause')
FUhA_clause.resultsName = 'FUhA_clause'
FUhA_post = Forward().setName('FUhA_post')
FUhA_post.resultsName = 'FUhA_post'
FUhA_pre = Forward().setName('FUhA_pre')
FUhA_pre.resultsName = 'FUhA_pre'
FUhE = Forward().setName('FUhE')
FUhE.resultsName = 'FUhE'
FUhE_clause = Forward().setName('FUhE_clause')
FUhE_clause.resultsName = 'FUhE_clause'
FUhE_post = Forward().setName('FUhE_post')
FUhE_post.resultsName = 'FUhE_post'
FUhE_pre = Forward().setName('FUhE_pre')
FUhE_pre.resultsName = 'FUhE_pre'
FUhO = Forward().setName('FUhO')
FUhO.resultsName = 'FUhO'
FUhO_clause = Forward().setName('FUhO_clause')
FUhO_clause.resultsName = 'FUhO_clause'
FUhO_post = Forward().setName('FUhO_post')
FUhO_post.resultsName = 'FUhO_post'
FUhO_pre = Forward().setName('FUhO_pre')
FUhO_pre.resultsName = 'FUhO_pre'
GA = Forward().setName('GA')
GA.resultsName = 'GA'
GA_clause = Forward().setName('GA_clause')
GA_clause.resultsName = 'GA_clause'
GA_post = Forward().setName('GA_post')
GA_post.resultsName = 'GA_post'
GA_pre = Forward().setName('GA_pre')
GA_pre.resultsName = 'GA_pre'
GAhO = Forward().setName('GAhO')
GAhO.resultsName = 'GAhO'
GAhO_clause = Forward().setName('GAhO_clause')
GAhO_clause.resultsName = 'GAhO_clause'
GAhO_post = Forward().setName('GAhO_post')
GAhO_post.resultsName = 'GAhO_post'
GAhO_pre = Forward().setName('GAhO_pre')
GAhO_pre.resultsName = 'GAhO_pre'
GEhU = Forward().setName('GEhU')
GEhU.resultsName = 'GEhU'
GEhU_clause = Forward().setName('GEhU_clause')
GEhU_clause.resultsName = 'GEhU_clause'
GEhU_post = Forward().setName('GEhU_post')
GEhU_post.resultsName = 'GEhU_post'
GEhU_pre = Forward().setName('GEhU_pre')
GEhU_pre.resultsName = 'GEhU_pre'
GI = Forward().setName('GI')
GI.resultsName = 'GI'
GI_clause = Forward().setName('GI_clause')
GI_clause.resultsName = 'GI_clause'
GI_post = Forward().setName('GI_post')
GI_post.resultsName = 'GI_post'
GI_pre = Forward().setName('GI_pre')
GI_pre.resultsName = 'GI_pre'
GIhA = Forward().setName('GIhA')
GIhA.resultsName = 'GIhA'
GIhA_clause = Forward().setName('GIhA_clause')
GIhA_clause.resultsName = 'GIhA_clause'
GIhA_post = Forward().setName('GIhA_post')
GIhA_post.resultsName = 'GIhA_post'
GIhA_pre = Forward().setName('GIhA_pre')
GIhA_pre.resultsName = 'GIhA_pre'
GOI = Forward().setName('GOI')
GOI.resultsName = 'GOI'
GOI_clause = Forward().setName('GOI_clause')
GOI_clause.resultsName = 'GOI_clause'
GOI_post = Forward().setName('GOI_post')
GOI_post.resultsName = 'GOI_post'
GOI_pre = Forward().setName('GOI_pre')
GOI_pre.resultsName = 'GOI_pre'
GOhA = Forward().setName('GOhA')
GOhA.resultsName = 'GOhA'
GOhA_clause = Forward().setName('GOhA_clause')
GOhA_clause.resultsName = 'GOhA_clause'
GOhA_post = Forward().setName('GOhA_post')
GOhA_post.resultsName = 'GOhA_post'
GOhA_pre = Forward().setName('GOhA_pre')
GOhA_pre.resultsName = 'GOhA_pre'
GUhA = Forward().setName('GUhA')
GUhA.resultsName = 'GUhA'
GUhA_clause = Forward().setName('GUhA_clause')
GUhA_clause.resultsName = 'GUhA_clause'
GUhA_post = Forward().setName('GUhA_post')
GUhA_post.resultsName = 'GUhA_post'
GUhA_pre = Forward().setName('GUhA_pre')
GUhA_pre.resultsName = 'GUhA_pre'
I = Forward().setName('I')
I.resultsName = 'I'
I_clause = Forward().setName('I_clause')
I_clause.resultsName = 'I_clause'
I_post = Forward().setName('I_post')
I_post.resultsName = 'I_post'
I_pre = Forward().setName('I_pre')
I_pre.resultsName = 'I_pre'
JA = Forward().setName('JA')
JA.resultsName = 'JA'
JA_clause = Forward().setName('JA_clause')
JA_clause.resultsName = 'JA_clause'
JA_post = Forward().setName('JA_post')
JA_post.resultsName = 'JA_post'
JA_pre = Forward().setName('JA_pre')
JA_pre.resultsName = 'JA_pre'
JAI = Forward().setName('JAI')
JAI.resultsName = 'JAI'
JAI_clause = Forward().setName('JAI_clause')
JAI_clause.resultsName = 'JAI_clause'
JAI_post = Forward().setName('JAI_post')
JAI_post.resultsName = 'JAI_post'
JAI_pre = Forward().setName('JAI_pre')
JAI_pre.resultsName = 'JAI_pre'
JOI = Forward().setName('JOI')
JOI.resultsName = 'JOI'
JOI_clause = Forward().setName('JOI_clause')
JOI_clause.resultsName = 'JOI_clause'
JOI_post = Forward().setName('JOI_post')
JOI_post.resultsName = 'JOI_post'
JOI_pre = Forward().setName('JOI_pre')
JOI_pre.resultsName = 'JOI_pre'
JOhI = Forward().setName('JOhI')
JOhI.resultsName = 'JOhI'
JOhI_clause = Forward().setName('JOhI_clause')
JOhI_clause.resultsName = 'JOhI_clause'
JOhI_post = Forward().setName('JOhI_post')
JOhI_post.resultsName = 'JOhI_post'
JOhI_pre = Forward().setName('JOhI_pre')
JOhI_pre.resultsName = 'JOhI_pre'
KE = Forward().setName('KE')
KE.resultsName = 'KE'
KE_clause = Forward().setName('KE_clause')
KE_clause.resultsName = 'KE_clause'
KE_post = Forward().setName('KE_post')
KE_post.resultsName = 'KE_post'
KE_pre = Forward().setName('KE_pre')
KE_pre.resultsName = 'KE_pre'
KEI = Forward().setName('KEI')
KEI.resultsName = 'KEI'
KEI_clause = Forward().setName('KEI_clause')
KEI_clause.resultsName = 'KEI_clause'
KEI_post = Forward().setName('KEI_post')
KEI_post.resultsName = 'KEI_post'
KEI_pre = Forward().setName('KEI_pre')
KEI_pre.resultsName = 'KEI_pre'
KEhE = Forward().setName('KEhE')
KEhE.resultsName = 'KEhE'
KEhE_clause = Forward().setName('KEhE_clause')
KEhE_clause.resultsName = 'KEhE_clause'
KEhE_post = Forward().setName('KEhE_post')
KEhE_post.resultsName = 'KEhE_post'
KEhE_pre = Forward().setName('KEhE_pre')
KEhE_pre.resultsName = 'KEhE_pre'
KI = Forward().setName('KI')
KI.resultsName = 'KI'
KI_clause = Forward().setName('KI_clause')
KI_clause.resultsName = 'KI_clause'
KI_post = Forward().setName('KI_post')
KI_post.resultsName = 'KI_post'
KI_pre = Forward().setName('KI_pre')
KI_pre.resultsName = 'KI_pre'
KOhA = Forward().setName('KOhA')
KOhA.resultsName = 'KOhA'
KOhA_clause = Forward().setName('KOhA_clause')
KOhA_clause.resultsName = 'KOhA_clause'
KOhA_post = Forward().setName('KOhA_post')
KOhA_post.resultsName = 'KOhA_post'
KOhA_pre = Forward().setName('KOhA_pre')
KOhA_pre.resultsName = 'KOhA_pre'
KU = Forward().setName('KU')
KU.resultsName = 'KU'
KU_clause = Forward().setName('KU_clause')
KU_clause.resultsName = 'KU_clause'
KU_post = Forward().setName('KU_post')
KU_post.resultsName = 'KU_post'
KU_pre = Forward().setName('KU_pre')
KU_pre.resultsName = 'KU_pre'
KUhE = Forward().setName('KUhE')
KUhE.resultsName = 'KUhE'
KUhE_clause = Forward().setName('KUhE_clause')
KUhE_clause.resultsName = 'KUhE_clause'
KUhE_post = Forward().setName('KUhE_post')
KUhE_post.resultsName = 'KUhE_post'
KUhE_pre = Forward().setName('KUhE_pre')
KUhE_pre.resultsName = 'KUhE_pre'
KUhO = Forward().setName('KUhO')
KUhO.resultsName = 'KUhO'
KUhO_clause = Forward().setName('KUhO_clause')
KUhO_clause.resultsName = 'KUhO_clause'
KUhO_post = Forward().setName('KUhO_post')
KUhO_post.resultsName = 'KUhO_post'
KUhO_pre = Forward().setName('KUhO_pre')
KUhO_pre.resultsName = 'KUhO_pre'
LA = Forward().setName('LA')
LA.resultsName = 'LA'
LA_clause = Forward().setName('LA_clause')
LA_clause.resultsName = 'LA_clause'
LA_post = Forward().setName('LA_post')
LA_post.resultsName = 'LA_post'
LA_pre = Forward().setName('LA_pre')
LA_pre.resultsName = 'LA_pre'
LAU = Forward().setName('LAU')
LAU.resultsName = 'LAU'
LAU_clause = Forward().setName('LAU_clause')
LAU_clause.resultsName = 'LAU_clause'
LAU_post = Forward().setName('LAU_post')
LAU_post.resultsName = 'LAU_post'
LAU_pre = Forward().setName('LAU_pre')
LAU_pre.resultsName = 'LAU_pre'
LAhE = Forward().setName('LAhE')
LAhE.resultsName = 'LAhE'
LAhE_clause = Forward().setName('LAhE_clause')
LAhE_clause.resultsName = 'LAhE_clause'
LAhE_post = Forward().setName('LAhE_post')
LAhE_post.resultsName = 'LAhE_post'
LAhE_pre = Forward().setName('LAhE_pre')
LAhE_pre.resultsName = 'LAhE_pre'
LE = Forward().setName('LE')
LE.resultsName = 'LE'
LE_clause = Forward().setName('LE_clause')
LE_clause.resultsName = 'LE_clause'
LE_post = Forward().setName('LE_post')
LE_post.resultsName = 'LE_post'
LE_pre = Forward().setName('LE_pre')
LE_pre.resultsName = 'LE_pre'
LEhU = Forward().setName('LEhU')
LEhU.resultsName = 'LEhU'
LEhU_clause = Forward().setName('LEhU_clause')
LEhU_clause.resultsName = 'LEhU_clause'
LEhU_post = Forward().setName('LEhU_post')
LEhU_post.resultsName = 'LEhU_post'
LEhU_pre = Forward().setName('LEhU_pre')
LEhU_pre.resultsName = 'LEhU_pre'
LI = Forward().setName('LI')
LI.resultsName = 'LI'
LI_clause = Forward().setName('LI_clause')
LI_clause.resultsName = 'LI_clause'
LI_post = Forward().setName('LI_post')
LI_post.resultsName = 'LI_post'
LI_pre = Forward().setName('LI_pre')
LI_pre.resultsName = 'LI_pre'
LIhU = Forward().setName('LIhU')
LIhU.resultsName = 'LIhU'
LIhU_clause = Forward().setName('LIhU_clause')
LIhU_clause.resultsName = 'LIhU_clause'
LIhU_post = Forward().setName('LIhU_post')
LIhU_post.resultsName = 'LIhU_post'
LIhU_pre = Forward().setName('LIhU_pre')
LIhU_pre.resultsName = 'LIhU_pre'
LOhO = Forward().setName('LOhO')
LOhO.resultsName = 'LOhO'
LOhO_clause = Forward().setName('LOhO_clause')
LOhO_clause.resultsName = 'LOhO_clause'
LOhO_post = Forward().setName('LOhO_post')
LOhO_post.resultsName = 'LOhO_post'
LOhO_pre = Forward().setName('LOhO_pre')
LOhO_pre.resultsName = 'LOhO_pre'
LOhU = Forward().setName('LOhU')
LOhU.resultsName = 'LOhU'
LOhU_clause = Forward().setName('LOhU_clause')
LOhU_clause.resultsName = 'LOhU_clause'
LOhU_post = Forward().setName('LOhU_post')
LOhU_post.resultsName = 'LOhU_post'
LOhU_pre = Forward().setName('LOhU_pre')
LOhU_pre.resultsName = 'LOhU_pre'
LU = Forward().setName('LU')
LU.resultsName = 'LU'
LU_clause = Forward().setName('LU_clause')
LU_clause.resultsName = 'LU_clause'
LU_post = Forward().setName('LU_post')
LU_post.resultsName = 'LU_post'
LU_pre = Forward().setName('LU_pre')
LU_pre.resultsName = 'LU_pre'
LUhU = Forward().setName('LUhU')
LUhU.resultsName = 'LUhU'
LUhU_clause = Forward().setName('LUhU_clause')
LUhU_clause.resultsName = 'LUhU_clause'
LUhU_post = Forward().setName('LUhU_post')
LUhU_post.resultsName = 'LUhU_post'
LUhU_pre = Forward().setName('LUhU_pre')
LUhU_pre.resultsName = 'LUhU_pre'
MAI = Forward().setName('MAI')
MAI.resultsName = 'MAI'
MAI_clause = Forward().setName('MAI_clause')
MAI_clause.resultsName = 'MAI_clause'
MAI_post = Forward().setName('MAI_post')
MAI_post.resultsName = 'MAI_post'
MAI_pre = Forward().setName('MAI_pre')
MAI_pre.resultsName = 'MAI_pre'
MAhO = Forward().setName('MAhO')
MAhO.resultsName = 'MAhO'
MAhO_clause = Forward().setName('MAhO_clause')
MAhO_clause.resultsName = 'MAhO_clause'
MAhO_post = Forward().setName('MAhO_post')
MAhO_post.resultsName = 'MAhO_post'
MAhO_pre = Forward().setName('MAhO_pre')
MAhO_pre.resultsName = 'MAhO_pre'
ME = Forward().setName('ME')
ME.resultsName = 'ME'
ME_clause = Forward().setName('ME_clause')
ME_clause.resultsName = 'ME_clause'
ME_post = Forward().setName('ME_post')
ME_post.resultsName = 'ME_post'
ME_pre = Forward().setName('ME_pre')
ME_pre.resultsName = 'ME_pre'
MEhU = Forward().setName('MEhU')
MEhU.resultsName = 'MEhU'
MEhU_clause = Forward().setName('MEhU_clause')
MEhU_clause.resultsName = 'MEhU_clause'
MEhU_post = Forward().setName('MEhU_post')
MEhU_post.resultsName = 'MEhU_post'
MEhU_pre = Forward().setName('MEhU_pre')
MEhU_pre.resultsName = 'MEhU_pre'
MOI = Forward().setName('MOI')
MOI.resultsName = 'MOI'
MOI_clause = Forward().setName('MOI_clause')
MOI_clause.resultsName = 'MOI_clause'
MOI_post = Forward().setName('MOI_post')
MOI_post.resultsName = 'MOI_post'
MOI_pre = Forward().setName('MOI_pre')
MOI_pre.resultsName = 'MOI_pre'
MOhE = Forward().setName('MOhE')
MOhE.resultsName = 'MOhE'
MOhE_clause = Forward().setName('MOhE_clause')
MOhE_clause.resultsName = 'MOhE_clause'
MOhE_post = Forward().setName('MOhE_post')
MOhE_post.resultsName = 'MOhE_post'
MOhE_pre = Forward().setName('MOhE_pre')
MOhE_pre.resultsName = 'MOhE_pre'
MOhI = Forward().setName('MOhI')
MOhI.resultsName = 'MOhI'
MOhI_clause = Forward().setName('MOhI_clause')
MOhI_clause.resultsName = 'MOhI_clause'
MOhI_post = Forward().setName('MOhI_post')
MOhI_post.resultsName = 'MOhI_post'
MOhI_pre = Forward().setName('MOhI_pre')
MOhI_pre.resultsName = 'MOhI_pre'
NA = Forward().setName('NA')
NA.resultsName = 'NA'
NA_clause = Forward().setName('NA_clause')
NA_clause.resultsName = 'NA_clause'
NA_post = Forward().setName('NA_post')
NA_post.resultsName = 'NA_post'
NA_pre = Forward().setName('NA_pre')
NA_pre.resultsName = 'NA_pre'
NAI = Forward().setName('NAI')
NAI.resultsName = 'NAI'
NAI_clause = Forward().setName('NAI_clause')
NAI_clause.resultsName = 'NAI_clause'
NAI_post = Forward().setName('NAI_post')
NAI_post.resultsName = 'NAI_post'
NAI_pre = Forward().setName('NAI_pre')
NAI_pre.resultsName = 'NAI_pre'
NAhE = Forward().setName('NAhE')
NAhE.resultsName = 'NAhE'
NAhE_clause = Forward().setName('NAhE_clause')
NAhE_clause.resultsName = 'NAhE_clause'
NAhE_post = Forward().setName('NAhE_post')
NAhE_post.resultsName = 'NAhE_post'
NAhE_pre = Forward().setName('NAhE_pre')
NAhE_pre.resultsName = 'NAhE_pre'
NAhU = Forward().setName('NAhU')
NAhU.resultsName = 'NAhU'
NAhU_clause = Forward().setName('NAhU_clause')
NAhU_clause.resultsName = 'NAhU_clause'
NAhU_post = Forward().setName('NAhU_post')
NAhU_post.resultsName = 'NAhU_post'
NAhU_pre = Forward().setName('NAhU_pre')
NAhU_pre.resultsName = 'NAhU_pre'
NIhE = Forward().setName('NIhE')
NIhE.resultsName = 'NIhE'
NIhE_clause = Forward().setName('NIhE_clause')
NIhE_clause.resultsName = 'NIhE_clause'
NIhE_post = Forward().setName('NIhE_post')
NIhE_post.resultsName = 'NIhE_post'
NIhE_pre = Forward().setName('NIhE_pre')
NIhE_pre.resultsName = 'NIhE_pre'
NIhO = Forward().setName('NIhO')
NIhO.resultsName = 'NIhO'
NIhO_clause = Forward().setName('NIhO_clause')
NIhO_clause.resultsName = 'NIhO_clause'
NIhO_post = Forward().setName('NIhO_post')
NIhO_post.resultsName = 'NIhO_post'
NIhO_pre = Forward().setName('NIhO_pre')
NIhO_pre.resultsName = 'NIhO_pre'
NOI = Forward().setName('NOI')
NOI.resultsName = 'NOI'
NOI_clause = Forward().setName('NOI_clause')
NOI_clause.resultsName = 'NOI_clause'
NOI_post = Forward().setName('NOI_post')
NOI_post.resultsName = 'NOI_post'
NOI_pre = Forward().setName('NOI_pre')
NOI_pre.resultsName = 'NOI_pre'
NU = Forward().setName('NU')
NU.resultsName = 'NU'
NU_clause = Forward().setName('NU_clause')
NU_clause.resultsName = 'NU_clause'
NU_post = Forward().setName('NU_post')
NU_post.resultsName = 'NU_post'
NU_pre = Forward().setName('NU_pre')
NU_pre.resultsName = 'NU_pre'
NUhA = Forward().setName('NUhA')
NUhA.resultsName = 'NUhA'
NUhA_clause = Forward().setName('NUhA_clause')
NUhA_clause.resultsName = 'NUhA_clause'
NUhA_post = Forward().setName('NUhA_post')
NUhA_post.resultsName = 'NUhA_post'
NUhA_pre = Forward().setName('NUhA_pre')
NUhA_pre.resultsName = 'NUhA_pre'
NUhI = Forward().setName('NUhI')
NUhI.resultsName = 'NUhI'
NUhI_clause = Forward().setName('NUhI_clause')
NUhI_clause.resultsName = 'NUhI_clause'
NUhI_post = Forward().setName('NUhI_post')
NUhI_post.resultsName = 'NUhI_post'
NUhI_pre = Forward().setName('NUhI_pre')
NUhI_pre.resultsName = 'NUhI_pre'
NUhU = Forward().setName('NUhU')
NUhU.resultsName = 'NUhU'
NUhU_clause = Forward().setName('NUhU_clause')
NUhU_clause.resultsName = 'NUhU_clause'
NUhU_post = Forward().setName('NUhU_post')
NUhU_post.resultsName = 'NUhU_post'
NUhU_pre = Forward().setName('NUhU_pre')
NUhU_pre.resultsName = 'NUhU_pre'
PA = Forward().setName('PA')
PA.resultsName = 'PA'
PA_clause = Forward().setName('PA_clause')
PA_clause.resultsName = 'PA_clause'
PA_post = Forward().setName('PA_post')
PA_post.resultsName = 'PA_post'
PA_pre = Forward().setName('PA_pre')
PA_pre.resultsName = 'PA_pre'
PEhE = Forward().setName('PEhE')
PEhE.resultsName = 'PEhE'
PEhE_clause = Forward().setName('PEhE_clause')
PEhE_clause.resultsName = 'PEhE_clause'
PEhE_post = Forward().setName('PEhE_post')
PEhE_post.resultsName = 'PEhE_post'
PEhE_pre = Forward().setName('PEhE_pre')
PEhE_pre.resultsName = 'PEhE_pre'
PEhO = Forward().setName('PEhO')
PEhO.resultsName = 'PEhO'
PEhO_clause = Forward().setName('PEhO_clause')
PEhO_clause.resultsName = 'PEhO_clause'
PEhO_post = Forward().setName('PEhO_post')
PEhO_post.resultsName = 'PEhO_post'
PEhO_pre = Forward().setName('PEhO_pre')
PEhO_pre.resultsName = 'PEhO_pre'
PU = Forward().setName('PU')
PU.resultsName = 'PU'
PU_clause = Forward().setName('PU_clause')
PU_clause.resultsName = 'PU_clause'
PU_post = Forward().setName('PU_post')
PU_post.resultsName = 'PU_post'
PU_pre = Forward().setName('PU_pre')
PU_pre.resultsName = 'PU_pre'
RAhO = Forward().setName('RAhO')
RAhO.resultsName = 'RAhO'
RAhO_clause = Forward().setName('RAhO_clause')
RAhO_clause.resultsName = 'RAhO_clause'
RAhO_post = Forward().setName('RAhO_post')
RAhO_post.resultsName = 'RAhO_post'
RAhO_pre = Forward().setName('RAhO_pre')
RAhO_pre.resultsName = 'RAhO_pre'
ROI = Forward().setName('ROI')
ROI.resultsName = 'ROI'
ROI_clause = Forward().setName('ROI_clause')
ROI_clause.resultsName = 'ROI_clause'
ROI_post = Forward().setName('ROI_post')
ROI_post.resultsName = 'ROI_post'
ROI_pre = Forward().setName('ROI_pre')
ROI_pre.resultsName = 'ROI_pre'
SA = Forward().setName('SA')
SA.resultsName = 'SA'
SA_clause = Forward().setName('SA_clause')
SA_clause.resultsName = 'SA_clause'
SA_post = Forward().setName('SA_post')
SA_post.resultsName = 'SA_post'
SA_pre = Forward().setName('SA_pre')
SA_pre.resultsName = 'SA_pre'
SE = Forward().setName('SE')
SE.resultsName = 'SE'
SE_clause = Forward().setName('SE_clause')
SE_clause.resultsName = 'SE_clause'
SE_post = Forward().setName('SE_post')
SE_post.resultsName = 'SE_post'
SE_pre = Forward().setName('SE_pre')
SE_pre.resultsName = 'SE_pre'
SEI = Forward().setName('SEI')
SEI.resultsName = 'SEI'
SEI_clause = Forward().setName('SEI_clause')
SEI_clause.resultsName = 'SEI_clause'
SEI_post = Forward().setName('SEI_post')
SEI_post.resultsName = 'SEI_post'
SEI_pre = Forward().setName('SEI_pre')
SEI_pre.resultsName = 'SEI_pre'
SEhU = Forward().setName('SEhU')
SEhU.resultsName = 'SEhU'
SEhU_clause = Forward().setName('SEhU_clause')
SEhU_clause.resultsName = 'SEhU_clause'
SEhU_post = Forward().setName('SEhU_post')
SEhU_post.resultsName = 'SEhU_post'
SEhU_pre = Forward().setName('SEhU_pre')
SEhU_pre.resultsName = 'SEhU_pre'
SI = Forward().setName('SI')
SI.resultsName = 'SI'
SI_clause = Forward().setName('SI_clause')
SI_clause.resultsName = 'SI_clause'
SOI = Forward().setName('SOI')
SOI.resultsName = 'SOI'
SOI_clause = Forward().setName('SOI_clause')
SOI_clause.resultsName = 'SOI_clause'
SOI_post = Forward().setName('SOI_post')
SOI_post.resultsName = 'SOI_post'
SOI_pre = Forward().setName('SOI_pre')
SOI_pre.resultsName = 'SOI_pre'
SU = Forward().setName('SU')
SU.resultsName = 'SU'
SU_clause = Forward().setName('SU_clause')
SU_clause.resultsName = 'SU_clause'
SU_post = Forward().setName('SU_post')
SU_post.resultsName = 'SU_post'
SU_pre = Forward().setName('SU_pre')
SU_pre.resultsName = 'SU_pre'
TAhE = Forward().setName('TAhE')
TAhE.resultsName = 'TAhE'
TAhE_clause = Forward().setName('TAhE_clause')
TAhE_clause.resultsName = 'TAhE_clause'
TAhE_post = Forward().setName('TAhE_post')
TAhE_post.resultsName = 'TAhE_post'
TAhE_pre = Forward().setName('TAhE_pre')
TAhE_pre.resultsName = 'TAhE_pre'
TEI = Forward().setName('TEI')
TEI.resultsName = 'TEI'
TEI_clause = Forward().setName('TEI_clause')
TEI_clause.resultsName = 'TEI_clause'
TEI_post = Forward().setName('TEI_post')
TEI_post.resultsName = 'TEI_post'
TEI_pre = Forward().setName('TEI_pre')
TEI_pre.resultsName = 'TEI_pre'
TEhU = Forward().setName('TEhU')
TEhU.resultsName = 'TEhU'
TEhU_clause = Forward().setName('TEhU_clause')
TEhU_clause.resultsName = 'TEhU_clause'
TEhU_post = Forward().setName('TEhU_post')
TEhU_post.resultsName = 'TEhU_post'
TEhU_pre = Forward().setName('TEhU_pre')
TEhU_pre.resultsName = 'TEhU_pre'
TO = Forward().setName('TO')
TO.resultsName = 'TO'
TO_clause = Forward().setName('TO_clause')
TO_clause.resultsName = 'TO_clause'
TO_post = Forward().setName('TO_post')
TO_post.resultsName = 'TO_post'
TO_pre = Forward().setName('TO_pre')
TO_pre.resultsName = 'TO_pre'
TOI = Forward().setName('TOI')
TOI.resultsName = 'TOI'
TOI_clause = Forward().setName('TOI_clause')
TOI_clause.resultsName = 'TOI_clause'
TOI_post = Forward().setName('TOI_post')
TOI_post.resultsName = 'TOI_post'
TOI_pre = Forward().setName('TOI_pre')
TOI_pre.resultsName = 'TOI_pre'
TUhE = Forward().setName('TUhE')
TUhE.resultsName = 'TUhE'
TUhE_clause = Forward().setName('TUhE_clause')
TUhE_clause.resultsName = 'TUhE_clause'
TUhE_post = Forward().setName('TUhE_post')
TUhE_post.resultsName = 'TUhE_post'
TUhE_pre = Forward().setName('TUhE_pre')
TUhE_pre.resultsName = 'TUhE_pre'
TUhU = Forward().setName('TUhU')
TUhU.resultsName = 'TUhU'
TUhU_clause = Forward().setName('TUhU_clause')
TUhU_clause.resultsName = 'TUhU_clause'
TUhU_post = Forward().setName('TUhU_post')
TUhU_post.resultsName = 'TUhU_post'
TUhU_pre = Forward().setName('TUhU_pre')
TUhU_pre.resultsName = 'TUhU_pre'
UI = Forward().setName('UI')
UI.resultsName = 'UI'
UI_clause = Forward().setName('UI_clause')
UI_clause.resultsName = 'UI_clause'
UI_post = Forward().setName('UI_post')
UI_post.resultsName = 'UI_post'
UI_pre = Forward().setName('UI_pre')
UI_pre.resultsName = 'UI_pre'
VA = Forward().setName('VA')
VA.resultsName = 'VA'
VA_clause = Forward().setName('VA_clause')
VA_clause.resultsName = 'VA_clause'
VA_post = Forward().setName('VA_post')
VA_post.resultsName = 'VA_post'
VA_pre = Forward().setName('VA_pre')
VA_pre.resultsName = 'VA_pre'
VAU = Forward().setName('VAU')
VAU.resultsName = 'VAU'
VAU_clause = Forward().setName('VAU_clause')
VAU_clause.resultsName = 'VAU_clause'
VAU_post = Forward().setName('VAU_post')
VAU_post.resultsName = 'VAU_post'
VAU_pre = Forward().setName('VAU_pre')
VAU_pre.resultsName = 'VAU_pre'
VEI = Forward().setName('VEI')
VEI.resultsName = 'VEI'
VEI_clause = Forward().setName('VEI_clause')
VEI_clause.resultsName = 'VEI_clause'
VEI_post = Forward().setName('VEI_post')
VEI_post.resultsName = 'VEI_post'
VEI_pre = Forward().setName('VEI_pre')
VEI_pre.resultsName = 'VEI_pre'
VEhA = Forward().setName('VEhA')
VEhA.resultsName = 'VEhA'
VEhA_clause = Forward().setName('VEhA_clause')
VEhA_clause.resultsName = 'VEhA_clause'
VEhA_post = Forward().setName('VEhA_post')
VEhA_post.resultsName = 'VEhA_post'
VEhA_pre = Forward().setName('VEhA_pre')
VEhA_pre.resultsName = 'VEhA_pre'
VEhO = Forward().setName('VEhO')
VEhO.resultsName = 'VEhO'
VEhO_clause = Forward().setName('VEhO_clause')
VEhO_clause.resultsName = 'VEhO_clause'
VEhO_post = Forward().setName('VEhO_post')
VEhO_post.resultsName = 'VEhO_post'
VEhO_pre = Forward().setName('VEhO_pre')
VEhO_pre.resultsName = 'VEhO_pre'
VIhA = Forward().setName('VIhA')
VIhA.resultsName = 'VIhA'
VIhA_clause = Forward().setName('VIhA_clause')
VIhA_clause.resultsName = 'VIhA_clause'
VIhA_post = Forward().setName('VIhA_post')
VIhA_post.resultsName = 'VIhA_post'
VIhA_pre = Forward().setName('VIhA_pre')
VIhA_pre.resultsName = 'VIhA_pre'
VUhO = Forward().setName('VUhO')
VUhO.resultsName = 'VUhO'
VUhO_clause = Forward().setName('VUhO_clause')
VUhO_clause.resultsName = 'VUhO_clause'
VUhO_post = Forward().setName('VUhO_post')
VUhO_post.resultsName = 'VUhO_post'
VUhO_pre = Forward().setName('VUhO_pre')
VUhO_pre.resultsName = 'VUhO_pre'
VUhU = Forward().setName('VUhU')
VUhU.resultsName = 'VUhU'
VUhU_clause = Forward().setName('VUhU_clause')
VUhU_clause.resultsName = 'VUhU_clause'
VUhU_post = Forward().setName('VUhU_post')
VUhU_post.resultsName = 'VUhU_post'
VUhU_pre = Forward().setName('VUhU_pre')
VUhU_pre.resultsName = 'VUhU_pre'
XI = Forward().setName('XI')
XI.resultsName = 'XI'
XI_clause = Forward().setName('XI_clause')
XI_clause.resultsName = 'XI_clause'
XI_post = Forward().setName('XI_post')
XI_post.resultsName = 'XI_post'
XI_pre = Forward().setName('XI_pre')
XI_pre.resultsName = 'XI_pre'
ZAhO = Forward().setName('ZAhO')
ZAhO.resultsName = 'ZAhO'
ZAhO_clause = Forward().setName('ZAhO_clause')
ZAhO_clause.resultsName = 'ZAhO_clause'
ZAhO_post = Forward().setName('ZAhO_post')
ZAhO_post.resultsName = 'ZAhO_post'
ZAhO_pre = Forward().setName('ZAhO_pre')
ZAhO_pre.resultsName = 'ZAhO_pre'
ZEI = Forward().setName('ZEI')
ZEI.resultsName = 'ZEI'
ZEI_clause = Forward().setName('ZEI_clause')
ZEI_clause.resultsName = 'ZEI_clause'
ZEI_post = Forward().setName('ZEI_post')
ZEI_post.resultsName = 'ZEI_post'
ZEI_pre = Forward().setName('ZEI_pre')
ZEI_pre.resultsName = 'ZEI_pre'
ZEhA = Forward().setName('ZEhA')
ZEhA.resultsName = 'ZEhA'
ZEhA_clause = Forward().setName('ZEhA_clause')
ZEhA_clause.resultsName = 'ZEhA_clause'
ZEhA_post = Forward().setName('ZEhA_post')
ZEhA_post.resultsName = 'ZEhA_post'
ZEhA_pre = Forward().setName('ZEhA_pre')
ZEhA_pre.resultsName = 'ZEhA_pre'
ZI = Forward().setName('ZI')
ZI.resultsName = 'ZI'
ZI_clause = Forward().setName('ZI_clause')
ZI_clause.resultsName = 'ZI_clause'
ZI_post = Forward().setName('ZI_post')
ZI_post.resultsName = 'ZI_post'
ZI_pre = Forward().setName('ZI_pre')
ZI_pre.resultsName = 'ZI_pre'
ZIhE = Forward().setName('ZIhE')
ZIhE.resultsName = 'ZIhE'
ZIhE_clause = Forward().setName('ZIhE_clause')
ZIhE_clause.resultsName = 'ZIhE_clause'
ZIhE_post = Forward().setName('ZIhE_post')
ZIhE_post.resultsName = 'ZIhE_post'
ZIhE_pre = Forward().setName('ZIhE_pre')
ZIhE_pre.resultsName = 'ZIhE_pre'
ZO = Forward().setName('ZO')
ZO.resultsName = 'ZO'
ZO_clause = Forward().setName('ZO_clause')
ZO_clause.resultsName = 'ZO_clause'
ZO_post = Forward().setName('ZO_post')
ZO_post.resultsName = 'ZO_post'
ZO_pre = Forward().setName('ZO_pre')
ZO_pre.resultsName = 'ZO_pre'
ZOI = Forward().setName('ZOI')
ZOI.resultsName = 'ZOI'
ZOI_clause = Forward().setName('ZOI_clause')
ZOI_clause.resultsName = 'ZOI_clause'
ZOI_post = Forward().setName('ZOI_post')
ZOI_post.resultsName = 'ZOI_post'
ZOI_pre = Forward().setName('ZOI_pre')
ZOI_pre.resultsName = 'ZOI_pre'
ZOhU = Forward().setName('ZOhU')
ZOhU.resultsName = 'ZOhU'
ZOhU_clause = Forward().setName('ZOhU_clause')
ZOhU_clause.resultsName = 'ZOhU_clause'
ZOhU_post = Forward().setName('ZOhU_post')
ZOhU_post.resultsName = 'ZOhU_post'
ZOhU_pre = Forward().setName('ZOhU_pre')
ZOhU_pre.resultsName = 'ZOhU_pre'
any_word = Forward().setName('any_word')
any_word.resultsName = 'any_word'
any_word_SA_handling = Forward().setName('any_word_SA_handling')
any_word_SA_handling.resultsName = 'any_word_SA_handling'
bridi_tail = Forward().setName('bridi_tail')
bridi_tail.resultsName = 'bridi_tail'
bridi_tail_1 = Forward().setName('bridi_tail_1')
bridi_tail_1.resultsName = 'bridi_tail_1'
bridi_tail_2 = Forward().setName('bridi_tail_2')
bridi_tail_2.resultsName = 'bridi_tail_2'
bridi_tail_3 = Forward().setName('bridi_tail_3')
bridi_tail_3.resultsName = 'bridi_tail_3'
bridi_tail_sa = Forward().setName('bridi_tail_sa')
bridi_tail_sa.resultsName = 'bridi_tail_sa'
bridi_tail_start = Forward().setName('bridi_tail_start')
bridi_tail_start.resultsName = 'bridi_tail_start'
bu_clause = Forward().setName('bu_clause')
bu_clause.resultsName = 'bu_clause'
bu_clause_no_pre = Forward().setName('bu_clause_no_pre')
bu_clause_no_pre.resultsName = 'bu_clause_no_pre'
bu_tail = Forward().setName('bu_tail')
bu_tail.resultsName = 'bu_tail'
cehe_sa = Forward().setName('cehe_sa')
cehe_sa.resultsName = 'cehe_sa'
ek = Forward().setName('ek')
ek.resultsName = 'ek'
erasable_clause = Forward().setName('erasable_clause')
erasable_clause.resultsName = 'erasable_clause'
faho_clause = Forward().setName('faho_clause')
faho_clause.resultsName = 'faho_clause'
fore_operands = Forward().setName('fore_operands')
fore_operands.resultsName = 'fore_operands'
fragment = Forward().setName('fragment')
fragment.resultsName = 'fragment'
free = Forward().setName('free')
free.resultsName = 'free'
gek = Forward().setName('gek')
gek.resultsName = 'gek'
gek_sentence = Forward().setName('gek_sentence')
gek_sentence.resultsName = 'gek_sentence'
gek_termset = Forward().setName('gek_termset')
gek_termset.resultsName = 'gek_termset'
gihek = Forward().setName('gihek')
gihek.resultsName = 'gihek'
gihek_1 = Forward().setName('gihek_1')
gihek_1.resultsName = 'gihek_1'
gihek_sa = Forward().setName('gihek_sa')
gihek_sa.resultsName = 'gihek_sa'
gik = Forward().setName('gik')
gik.resultsName = 'gik'
guhek = Forward().setName('guhek')
guhek.resultsName = 'guhek'
indicator = Forward().setName('indicator')
indicator.resultsName = 'indicator'
indicators = Forward().setName('indicators')
indicators.resultsName = 'indicators'
inner_word = Forward().setName('inner_word')
inner_word.resultsName = 'inner_word'
inner_word2 = Forward().setName('inner_word2')
inner_word2.resultsName = 'inner_word2'
interval = Forward().setName('interval')
interval.resultsName = 'interval'
interval_property = Forward().setName('interval_property')
interval_property.resultsName = 'interval_property'
intro_null = Forward().setName('intro_null')
intro_null.resultsName = 'intro_null'
intro_si_clause = Forward().setName('intro_si_clause')
intro_si_clause.resultsName = 'intro_si_clause'
jek = Forward().setName('jek')
jek.resultsName = 'jek'
joik = Forward().setName('joik')
joik.resultsName = 'joik'
joik_ek = Forward().setName('joik_ek')
joik_ek.resultsName = 'joik_ek'
joik_ek_1 = Forward().setName('joik_ek_1')
joik_ek_1.resultsName = 'joik_ek_1'
joik_ek_sa = Forward().setName('joik_ek_sa')
joik_ek_sa.resultsName = 'joik_ek_sa'
joik_jek = Forward().setName('joik_jek')
joik_jek.resultsName = 'joik_jek'
known_cmavo_SA = Forward().setName('known_cmavo_SA')
known_cmavo_SA.resultsName = 'known_cmavo_SA'
lerfu_string = Forward().setName('lerfu_string')
lerfu_string.resultsName = 'lerfu_string'
lerfu_word = Forward().setName('lerfu_word')
lerfu_word.resultsName = 'lerfu_word'
li_clause = Forward().setName('li_clause')
li_clause.resultsName = 'li_clause'
linkargs = Forward().setName('linkargs')
linkargs.resultsName = 'linkargs'
linkargs_1 = Forward().setName('linkargs_1')
linkargs_1.resultsName = 'linkargs_1'
linkargs_sa = Forward().setName('linkargs_sa')
linkargs_sa.resultsName = 'linkargs_sa'
linkargs_start = Forward().setName('linkargs_start')
linkargs_start.resultsName = 'linkargs_start'
links = Forward().setName('links')
links.resultsName = 'links'
links_1 = Forward().setName('links_1')
links_1.resultsName = 'links_1'
links_sa = Forward().setName('links_sa')
links_sa.resultsName = 'links_sa'
links_start = Forward().setName('links_start')
links_start.resultsName = 'links_start'
mex = Forward().setName('mex')
mex.resultsName = 'mex'
mex_0 = Forward().setName('mex_0')
mex_0.resultsName = 'mex_0'
mex_1 = Forward().setName('mex_1')
mex_1.resultsName = 'mex_1'
mex_2 = Forward().setName('mex_2')
mex_2.resultsName = 'mex_2'
mex_forethought = Forward().setName('mex_forethought')
mex_forethought.resultsName = 'mex_forethought'
mex_operator = Forward().setName('mex_operator')
mex_operator.resultsName = 'mex_operator'
mex_sa = Forward().setName('mex_sa')
mex_sa.resultsName = 'mex_sa'
mex_start = Forward().setName('mex_start')
mex_start.resultsName = 'mex_start'
number = Forward().setName('number')
number.resultsName = 'number'
operand = Forward().setName('operand')
operand.resultsName = 'operand'
operand_0 = Forward().setName('operand_0')
operand_0.resultsName = 'operand_0'
operand_1 = Forward().setName('operand_1')
operand_1.resultsName = 'operand_1'
operand_2 = Forward().setName('operand_2')
operand_2.resultsName = 'operand_2'
operand_3 = Forward().setName('operand_3')
operand_3.resultsName = 'operand_3'
operand_sa = Forward().setName('operand_sa')
operand_sa.resultsName = 'operand_sa'
operand_start = Forward().setName('operand_start')
operand_start.resultsName = 'operand_start'
operator = Forward().setName('operator')
operator.resultsName = 'operator'
operator_0 = Forward().setName('operator_0')
operator_0.resultsName = 'operator_0'
operator_1 = Forward().setName('operator_1')
operator_1.resultsName = 'operator_1'
operator_2 = Forward().setName('operator_2')
operator_2.resultsName = 'operator_2'
operator_sa = Forward().setName('operator_sa')
operator_sa.resultsName = 'operator_sa'
operator_start = Forward().setName('operator_start')
operator_start.resultsName = 'operator_start'
paragraph = Forward().setName('paragraph')
paragraph.resultsName = 'paragraph'
paragraphs = Forward().setName('paragraphs')
paragraphs.resultsName = 'paragraphs'
pehe_sa = Forward().setName('pehe_sa')
pehe_sa.resultsName = 'pehe_sa'
post_clause = Forward().setName('post_clause')
post_clause.resultsName = 'post_clause'
pre_clause = Forward().setName('pre_clause')
pre_clause.resultsName = 'pre_clause'
pre_zei_bu = Forward().setName('pre_zei_bu')
pre_zei_bu.resultsName = 'pre_zei_bu'
prenex = Forward().setName('prenex')
prenex.resultsName = 'prenex'
quantifier = Forward().setName('quantifier')
quantifier.resultsName = 'quantifier'
relative_clause = Forward().setName('relative_clause')
relative_clause.resultsName = 'relative_clause'
relative_clause_1 = Forward().setName('relative_clause_1')
relative_clause_1.resultsName = 'relative_clause_1'
relative_clause_sa = Forward().setName('relative_clause_sa')
relative_clause_sa.resultsName = 'relative_clause_sa'
relative_clause_start = Forward().setName('relative_clause_start')
relative_clause_start.resultsName = 'relative_clause_start'
relative_clauses = Forward().setName('relative_clauses')
relative_clauses.resultsName = 'relative_clauses'
rp_clause = Forward().setName('rp_clause')
rp_clause.resultsName = 'rp_clause'
rp_expression = Forward().setName('rp_expression')
rp_expression.resultsName = 'rp_expression'
rp_expression_tail = Forward().setName('rp_expression_tail')
rp_expression_tail.resultsName = 'rp_expression_tail'
sa_word = Forward().setName('sa_word')
sa_word.resultsName = 'sa_word'
selbri = Forward().setName('selbri')
selbri.resultsName = 'selbri'
selbri_1 = Forward().setName('selbri_1')
selbri_1.resultsName = 'selbri_1'
selbri_2 = Forward().setName('selbri_2')
selbri_2.resultsName = 'selbri_2'
selbri_3 = Forward().setName('selbri_3')
selbri_3.resultsName = 'selbri_3'
selbri_4 = Forward().setName('selbri_4')
selbri_4.resultsName = 'selbri_4'
selbri_5 = Forward().setName('selbri_5')
selbri_5.resultsName = 'selbri_5'
selbri_6 = Forward().setName('selbri_6')
selbri_6.resultsName = 'selbri_6'
sentence = Forward().setName('sentence')
sentence.resultsName = 'sentence'
sentence_sa = Forward().setName('sentence_sa')
sentence_sa.resultsName = 'sentence_sa'
sentence_start = Forward().setName('sentence_start')
sentence_start.resultsName = 'sentence_start'
si_clause = Forward().setName('si_clause')
si_clause.resultsName = 'si_clause'
si_word = Forward().setName('si_word')
si_word.resultsName = 'si_word'
simple_tense_modal = Forward().setName('simple_tense_modal')
simple_tense_modal.resultsName = 'simple_tense_modal'
space = Forward().setName('space')
space.resultsName = 'space'
space_int_props = Forward().setName('space_int_props')
space_int_props.resultsName = 'space_int_props'
space_interval = Forward().setName('space_interval')
space_interval.resultsName = 'space_interval'
space_offset = Forward().setName('space_offset')
space_offset.resultsName = 'space_offset'
spaces = Forward().setName('spaces')
spaces.resultsName = 'spaces'
stag = Forward().setName('stag')
stag.resultsName = 'stag'
statement = Forward().setName('statement')
statement.resultsName = 'statement'
statement_1 = Forward().setName('statement_1')
statement_1.resultsName = 'statement_1'
statement_2 = Forward().setName('statement_2')
statement_2.resultsName = 'statement_2'
statement_3 = Forward().setName('statement_3')
statement_3.resultsName = 'statement_3'
su_clause = Forward().setName('su_clause')
su_clause.resultsName = 'su_clause'
su_word = Forward().setName('su_word')
su_word.resultsName = 'su_word'
subsentence = Forward().setName('subsentence')
subsentence.resultsName = 'subsentence'
sumti = Forward().setName('sumti')
sumti.resultsName = 'sumti'
sumti_1 = Forward().setName('sumti_1')
sumti_1.resultsName = 'sumti_1'
sumti_2 = Forward().setName('sumti_2')
sumti_2.resultsName = 'sumti_2'
sumti_3 = Forward().setName('sumti_3')
sumti_3.resultsName = 'sumti_3'
sumti_4 = Forward().setName('sumti_4')
sumti_4.resultsName = 'sumti_4'
sumti_5 = Forward().setName('sumti_5')
sumti_5.resultsName = 'sumti_5'
sumti_6 = Forward().setName('sumti_6')
sumti_6.resultsName = 'sumti_6'
sumti_tail = Forward().setName('sumti_tail')
sumti_tail.resultsName = 'sumti_tail'
sumti_tail_1 = Forward().setName('sumti_tail_1')
sumti_tail_1.resultsName = 'sumti_tail_1'
tag = Forward().setName('tag')
tag.resultsName = 'tag'
tail_terms = Forward().setName('tail_terms')
tail_terms.resultsName = 'tail_terms'
tanru_unit = Forward().setName('tanru_unit')
tanru_unit.resultsName = 'tanru_unit'
tanru_unit_1 = Forward().setName('tanru_unit_1')
tanru_unit_1.resultsName = 'tanru_unit_1'
tanru_unit_2 = Forward().setName('tanru_unit_2')
tanru_unit_2.resultsName = 'tanru_unit_2'
tense_modal = Forward().setName('tense_modal')
tense_modal.resultsName = 'tense_modal'
term = Forward().setName('term')
term.resultsName = 'term'
term_1 = Forward().setName('term_1')
term_1.resultsName = 'term_1'
term_sa = Forward().setName('term_sa')
term_sa.resultsName = 'term_sa'
term_start = Forward().setName('term_start')
term_start.resultsName = 'term_start'
terms = Forward().setName('terms')
terms.resultsName = 'terms'
terms_1 = Forward().setName('terms_1')
terms_1.resultsName = 'terms_1'
terms_2 = Forward().setName('terms_2')
terms_2.resultsName = 'terms_2'
terms_gik_terms = Forward().setName('terms_gik_terms')
terms_gik_terms.resultsName = 'terms_gik_terms'
termset = Forward().setName('termset')
termset.resultsName = 'termset'
text = Forward().setName('text')
text.resultsName = 'text'
text_1 = Forward().setName('text_1')
text_1.resultsName = 'text_1'
text_part_2 = Forward().setName('text_part_2')
text_part_2.resultsName = 'text_part_2'
time = Forward().setName('time')
time.resultsName = 'time'
time_offset = Forward().setName('time_offset')
time_offset.resultsName = 'time_offset'
vocative = Forward().setName('vocative')
vocative.resultsName = 'vocative'
xi_clause = Forward().setName('xi_clause')
xi_clause.resultsName = 'xi_clause'
zei_clause = Forward().setName('zei_clause')
zei_clause.resultsName = 'zei_clause'
zei_clause_no_pre = Forward().setName('zei_clause_no_pre')
zei_clause_no_pre.resultsName = 'zei_clause_no_pre'
zei_tail = Forward().setName('zei_tail')
zei_tail.resultsName = 'zei_tail'

A << Group(A_word_pre + inner_word + close_paren + close_paren)
A_clause << Group(A_pre + A_post)
A_post << Group(post_clause)
A_pre << Group(pre_clause + A + Optional(spaces))
BAI << Group(BAI_word_pre + inner_word + close_paren + close_paren)
BAI_clause << Group(BAI_pre + BAI_post)
BAI_post << Group(post_clause)
BAI_pre << Group(pre_clause + BAI + Optional(spaces))
BAhE << Group(BAhE_word_pre + inner_word + close_paren + close_paren)
BAhE_clause << Group(OneOrMore(BAhE_pre + BAhE_post))
BAhE_post << Group(Optional(si_clause) + ~ZEI_clause + ~BU_clause)
BAhE_pre << Group(BAhE + Optional(spaces))
BE << Group(BE_word_pre + inner_word + close_paren + close_paren)
BE_clause << Group(BE_pre + BE_post)
BE_post << Group(post_clause)
BE_pre << Group(pre_clause + BE + Optional(spaces))
BEI << Group(BEI_word_pre + inner_word + close_paren + close_paren)
BEI_clause << Group(BEI_pre + BEI_post)
BEI_post << Group(post_clause)
BEI_pre << Group(pre_clause + BEI + Optional(spaces))
BEhO << Group(BEhO_word_pre + inner_word + close_paren + close_paren)
BEhO_clause << Group(BEhO_pre + BEhO_post)
BEhO_post << Group(post_clause)
BEhO_pre << Group(pre_clause + BEhO + Optional(spaces))
BIhE << Group(BIhE_word_pre + inner_word + close_paren + close_paren)
BIhE_clause << Group(BIhE_pre + BIhE_post)
BIhE_post << Group(post_clause)
BIhE_pre << Group(pre_clause + BIhE + Optional(spaces))
BIhI << Group(BIhI_word_pre + inner_word + close_paren + close_paren)
BIhI_clause << Group(BIhI_pre + BIhI_post)
BIhI_post << Group(post_clause)
BIhI_pre << Group(pre_clause + BIhI + Optional(spaces))
BO << Group(BO_word_pre + inner_word + close_paren + close_paren)
BO_clause << Group(BO_pre + BO_post)
BO_post << Group(post_clause)
BO_pre << Group(pre_clause + BO + Optional(spaces))
BOI << Group(BOI_word_pre + inner_word + close_paren + close_paren)
BOI_clause << Group(BOI_pre + BOI_post)
BOI_post << Group(post_clause)
BOI_pre << Group(pre_clause + BOI + Optional(spaces))
BRIVLA << Group(BRIVLA_word_pre + inner_word + close_paren)
BRIVLA_clause << Group(BRIVLA_pre + BRIVLA_post | zei_clause)
BRIVLA_post << Group(post_clause)
BRIVLA_pre << Group(pre_clause + BRIVLA + Optional(spaces))
BU << Group(BU_word_pre + inner_word + close_paren + close_paren)
BU_clause << Group(BU_pre + BU_post)
BU_post << Group(Optional(spaces))
BU_pre << Group(pre_clause + BU + Optional(spaces))
BY << Group(BY_word_pre + inner_word + close_paren + close_paren)
BY_clause << Group(BY_pre + BY_post | bu_clause)
BY_post << Group(post_clause)
BY_pre << Group(pre_clause + BY + Optional(spaces))
CAI << Group(CAI_word_pre + inner_word + close_paren + close_paren)
CAI_clause << Group(CAI_pre + CAI_post)
CAI_post << Group(post_clause)
CAI_pre << Group(pre_clause + CAI + Optional(spaces))
CAhA << Group(CAhA_word_pre + inner_word + close_paren + close_paren)
CAhA_clause << Group(CAhA_pre + CAhA_post)
CAhA_post << Group(post_clause)
CAhA_pre << Group(pre_clause + CAhA + Optional(spaces))
CEI << Group(CEI_word_pre + inner_word + close_paren + close_paren)
CEI_clause << Group(CEI_pre + CEI_post)
CEI_post << Group(post_clause)
CEI_pre << Group(pre_clause + CEI + Optional(spaces))
CEhE << Group(CEhE_word_pre + inner_word + close_paren + close_paren)
CEhE_clause << Group(CEhE_pre + CEhE_post)
CEhE_post << Group(post_clause)
CEhE_pre << Group(pre_clause + CEhE + Optional(spaces))
CMAVO << Group(CMAVO_word_pre + inner_word + close_paren)
CMAVO_pre << Group(pre_clause + CMAVO + Optional(spaces))
CMENE << Group(CMENE_word_pre + inner_word + close_paren)
CMENE_clause << Group(CMENE_pre + CMENE_post)
CMENE_post << Group(post_clause)
CMENE_pre << Group(pre_clause + CMENE + Optional(spaces))
CO << Group(CO_word_pre + inner_word + close_paren + close_paren)
CO_clause << Group(CO_pre + CO_post)
CO_post << Group(post_clause)
CO_pre << Group(pre_clause + CO + Optional(spaces))
COI << Group(COI_word_pre + inner_word + close_paren + close_paren)
COI_clause << Group(COI_pre + COI_post)
COI_post << Group(post_clause)
COI_pre << Group(pre_clause + COI + Optional(spaces))
CU << Group(CU_word_pre + inner_word + close_paren + close_paren)
CU_clause << Group(CU_pre + CU_post)
CU_post << Group(post_clause)
CU_pre << Group(pre_clause + CU + Optional(spaces))
CUhE << Group(CUhE_word_pre + inner_word + close_paren + close_paren)
CUhE_clause << Group(CUhE_pre + CUhE_post)
CUhE_post << Group(post_clause)
CUhE_pre << Group(pre_clause + CUhE + Optional(spaces))
DAhO << Group(DAhO_word_pre + inner_word + close_paren + close_paren)
DAhO_clause << Group(DAhO_pre + DAhO_post)
DAhO_post << Group(post_clause)
DAhO_pre << Group(pre_clause + DAhO + Optional(spaces))
DOI << Group(DOI_word_pre + inner_word + close_paren + close_paren)
DOI_clause << Group(DOI_pre + DOI_post)
DOI_post << Group(post_clause)
DOI_pre << Group(pre_clause + DOI + Optional(spaces))
DOhU << Group(DOhU_word_pre + inner_word + close_paren + close_paren)
DOhU_clause << Group(DOhU_pre + DOhU_post)
DOhU_post << Group(post_clause)
DOhU_pre << Group(pre_clause + DOhU + Optional(spaces))
FA << Group(FA_word_pre + inner_word + close_paren + close_paren)
FA_clause << Group(FA_pre + FA_post)
FA_post << Group(post_clause)
FA_pre << Group(pre_clause + FA + Optional(spaces))
FAhA << Group(FAhA_word_pre + inner_word + close_paren + close_paren)
FAhA_clause << Group(FAhA_pre + FAhA_post)
FAhA_post << Group(post_clause)
FAhA_pre << Group(pre_clause + FAhA + Optional(spaces))
FAhO << Group(FAhO_word_pre + inner_word + close_paren + close_paren)
FAhO_clause << Group(pre_clause + FAhO + Optional(spaces))
FEhE << Group(FEhE_word_pre + inner_word + close_paren + close_paren)
FEhE_clause << Group(FEhE_pre + FEhE_post)
FEhE_post << Group(post_clause)
FEhE_pre << Group(pre_clause + FEhE + Optional(spaces))
FEhU << Group(FEhU_word_pre + inner_word + close_paren + close_paren)
FEhU_clause << Group(FEhU_pre + FEhU_post)
FEhU_post << Group(post_clause)
FEhU_pre << Group(pre_clause + FEhU + Optional(spaces))
FIhO << Group(FIhO_word_pre + inner_word + close_paren + close_paren)
FIhO_clause << Group(FIhO_pre + FIhO_post)
FIhO_post << Group(post_clause)
FIhO_pre << Group(pre_clause + FIhO + Optional(spaces))
FOI << Group(FOI_word_pre + inner_word + close_paren + close_paren)
FOI_clause << Group(FOI_pre + FOI_post)
FOI_post << Group(post_clause)
FOI_pre << Group(pre_clause + FOI + Optional(spaces))
FUhA << Group(FUhA_word_pre + inner_word + close_paren + close_paren)
FUhA_clause << Group(FUhA_pre + FUhA_post)
FUhA_post << Group(post_clause)
FUhA_pre << Group(pre_clause + FUhA + Optional(spaces))
FUhE << Group(FUhE_word_pre + inner_word + close_paren + close_paren)
FUhE_clause << Group(FUhE_pre + FUhE_post)
FUhE_post << Group(~BU_clause + Optional(spaces) + ~ZEI_clause + ~BU_clause)
FUhE_pre << Group(pre_clause + FUhE + Optional(spaces))
FUhO << Group(FUhO_word_pre + inner_word + close_paren + close_paren)
FUhO_clause << Group(FUhO_pre + FUhO_post)
FUhO_post << Group(post_clause)
FUhO_pre << Group(pre_clause + FUhO + Optional(spaces))
GA << Group(GA_word_pre + inner_word + close_paren + close_paren)
GA_clause << Group(GA_pre + GA_post)
GA_post << Group(post_clause)
GA_pre << Group(pre_clause + GA + Optional(spaces))
GAhO << Group(GAhO_word_pre + inner_word + close_paren + close_paren)
GAhO_clause << Group(GAhO_pre + GAhO_post)
GAhO_post << Group(post_clause)
GAhO_pre << Group(pre_clause + GAhO + Optional(spaces))
GEhU << Group(GEhU_word_pre + inner_word + close_paren + close_paren)
GEhU_clause << Group(GEhU_pre + GEhU_post)
GEhU_post << Group(post_clause)
GEhU_pre << Group(pre_clause + GEhU + Optional(spaces))
GI << Group(GI_word_pre + inner_word + close_paren + close_paren)
GI_clause << Group(GI_pre + GI_post)
GI_post << Group(post_clause)
GI_pre << Group(pre_clause + GI + Optional(spaces))
GIhA << Group(GIhA_word_pre + inner_word + close_paren + close_paren)
GIhA_clause << Group(GIhA_pre + GIhA_post)
GIhA_post << Group(post_clause)
GIhA_pre << Group(pre_clause + GIhA + Optional(spaces))
GOI << Group(GOI_word_pre + inner_word + close_paren + close_paren)
GOI_clause << Group(GOI_pre + GOI_post)
GOI_post << Group(post_clause)
GOI_pre << Group(pre_clause + GOI + Optional(spaces))
GOhA << Group(GOhA_word_pre + inner_word + close_paren + close_paren)
GOhA_clause << Group(GOhA_pre + GOhA_post)
GOhA_post << Group(post_clause)
GOhA_pre << Group(pre_clause + GOhA + Optional(spaces))
GUhA << Group(GUhA_word_pre + inner_word + close_paren + close_paren)
GUhA_clause << Group(GUhA_pre + GUhA_post)
GUhA_post << Group(post_clause)
GUhA_pre << Group(pre_clause + GUhA + Optional(spaces))
I << Group(I_word_pre + inner_word + close_paren + close_paren)
I_clause << Group(ZeroOrMore(sentence_sa) + I_pre + I_post)
I_post << Group(post_clause)
I_pre << Group(pre_clause + I + Optional(spaces))
JA << Group(JA_word_pre + inner_word + close_paren + close_paren)
JA_clause << Group(JA_pre + JA_post)
JA_post << Group(post_clause)
JA_pre << Group(pre_clause + JA + Optional(spaces))
JAI << Group(JAI_word_pre + inner_word + close_paren + close_paren)
JAI_clause << Group(JAI_pre + JAI_post)
JAI_post << Group(post_clause)
JAI_pre << Group(pre_clause + JAI + Optional(spaces))
JOI << Group(JOI_word_pre + inner_word + close_paren + close_paren)
JOI_clause << Group(JOI_pre + JOI_post)
JOI_post << Group(post_clause)
JOI_pre << Group(pre_clause + JOI + Optional(spaces))
JOhI << Group(JOhI_word_pre + inner_word + close_paren + close_paren)
JOhI_clause << Group(JOhI_pre + JOhI_post)
JOhI_post << Group(post_clause)
JOhI_pre << Group(pre_clause + JOhI + Optional(spaces))
KE << Group(KE_word_pre + inner_word + close_paren + close_paren)
KE_clause << Group(KE_pre + KE_post)
KE_post << Group(post_clause)
KE_pre << Group(pre_clause + KE + Optional(spaces))
KEI << Group(KEI_word_pre + inner_word + close_paren + close_paren)
KEI_clause << Group(KEI_pre + KEI_post)
KEI_post << Group(post_clause)
KEI_pre << Group(pre_clause + KEI + Optional(spaces))
KEhE << Group(KEhE_word_pre + inner_word + close_paren + close_paren)
KEhE_clause << Group(KEhE_pre + KEhE_post)
KEhE_post << Group(post_clause)
KEhE_pre << Group(pre_clause + KEhE + Optional(spaces))
KI << Group(KI_word_pre + inner_word + close_paren + close_paren)
KI_clause << Group(KI_pre + KI_post)
KI_post << Group(post_clause)
KI_pre << Group(pre_clause + KI + Optional(spaces))
KOhA << Group(KOhA_word_pre + inner_word + close_paren + close_paren)
KOhA_clause << Group(KOhA_pre + KOhA_post)
KOhA_post << Group(post_clause)
KOhA_pre << Group(pre_clause + KOhA + Optional(spaces))
KU << Group(KU_word_pre + inner_word + close_paren + close_paren)
KU_clause << Group(KU_pre + KU_post)
KU_post << Group(post_clause)
KU_pre << Group(pre_clause + KU + Optional(spaces))
KUhE << Group(KUhE_word_pre + inner_word + close_paren + close_paren)
KUhE_clause << Group(KUhE_pre + KUhE_post)
KUhE_post << Group(post_clause)
KUhE_pre << Group(pre_clause + KUhE + Optional(spaces))
KUhO << Group(KUhO_word_pre + inner_word + close_paren + close_paren)
KUhO_clause << Group(KUhO_pre + KUhO_post)
KUhO_post << Group(post_clause)
KUhO_pre << Group(pre_clause + KUhO + Optional(spaces))
LA << Group(LA_word_pre + inner_word + close_paren + close_paren)
LA_clause << Group(LA_pre + LA_post)
LA_post << Group(post_clause)
LA_pre << Group(pre_clause + LA + Optional(spaces))
LAU << Group(LAU_word_pre + inner_word + close_paren + close_paren)
LAU_clause << Group(LAU_pre + LAU_post)
LAU_post << Group(post_clause)
LAU_pre << Group(pre_clause + LAU + Optional(spaces))
LAhE << Group(LAhE_word_pre + inner_word + close_paren + close_paren)
LAhE_clause << Group(LAhE_pre + LAhE_post)
LAhE_post << Group(post_clause)
LAhE_pre << Group(pre_clause + LAhE + Optional(spaces))
LE << Group(LE_word_pre + inner_word + close_paren + close_paren)
LE_clause << Group(LE_pre + LE_post)
LE_post << Group(post_clause)
LE_pre << Group(pre_clause + LE + Optional(spaces))
LEhU << Group(LEhU_word_pre + inner_word + close_paren + close_paren)
LEhU_clause << Group(LEhU_pre + LEhU_post)
LEhU_post << Group(Optional(spaces))
LEhU_pre << Group(pre_clause + LEhU + Optional(spaces))
LI << Group(LI_word_pre + inner_word + close_paren + close_paren)
LI_clause << Group(LI_pre + LI_post)
LI_post << Group(post_clause)
LI_pre << Group(pre_clause + LI + Optional(spaces))
LIhU << Group(LIhU_word_pre + inner_word + close_paren + close_paren)
LIhU_clause << Group(LIhU_pre + LIhU_post)
LIhU_post << Group(post_clause)
LIhU_pre << Group(pre_clause + LIhU + Optional(spaces))
LOhO << Group(LOhO_word_pre + inner_word + close_paren + close_paren)
LOhO_clause << Group(LOhO_pre + LOhO_post)
LOhO_post << Group(post_clause)
LOhO_pre << Group(pre_clause + LOhO + Optional(spaces))
LOhU << Group(LOhU_word_pre + inner_word + close_paren + close_paren)
LOhU_clause << Group(LOhU_pre + LOhU_post)
LOhU_post << Group(post_clause)
LOhU_pre << Group(pre_clause + LOhU + Optional(spaces) + ZeroOrMore(~LEhU + any_word) + LEhU_clause + Optional(spaces))
LU << Group(LU_word_pre + inner_word + close_paren + close_paren)
LU_clause << Group(LU_pre + LU_post)
LU_post << Group(post_clause)
LU_pre << Group(pre_clause + LU + Optional(spaces))
LUhU << Group(LUhU_word_pre + inner_word + close_paren + close_paren)
LUhU_clause << Group(LUhU_pre + LUhU_post)
LUhU_post << Group(post_clause)
LUhU_pre << Group(pre_clause + LUhU + Optional(spaces))
MAI << Group(MAI_word_pre + inner_word + close_paren + close_paren)
MAI_clause << Group(MAI_pre + MAI_post)
MAI_post << Group(post_clause)
MAI_pre << Group(pre_clause + MAI + Optional(spaces))
MAhO << Group(MAhO_word_pre + inner_word + close_paren + close_paren)
MAhO_clause << Group(MAhO_pre + MAhO_post)
MAhO_post << Group(post_clause)
MAhO_pre << Group(pre_clause + MAhO + Optional(spaces))
ME << Group(ME_word_pre + inner_word + close_paren + close_paren)
ME_clause << Group(ME_pre + ME_post)
ME_post << Group(post_clause)
ME_pre << Group(pre_clause + ME + Optional(spaces))
MEhU << Group(MEhU_word_pre + inner_word + close_paren + close_paren)
MEhU_clause << Group(MEhU_pre + MEhU_post)
MEhU_post << Group(post_clause)
MEhU_pre << Group(pre_clause + MEhU + Optional(spaces))
MOI << Group(MOI_word_pre + inner_word + close_paren + close_paren)
MOI_clause << Group(MOI_pre + MOI_post)
MOI_post << Group(post_clause)
MOI_pre << Group(pre_clause + MOI + Optional(spaces))
MOhE << Group(MOhE_word_pre + inner_word + close_paren + close_paren)
MOhE_clause << Group(MOhE_pre + MOhE_post)
MOhE_post << Group(post_clause)
MOhE_pre << Group(pre_clause + MOhE + Optional(spaces))
MOhI << Group(MOhI_word_pre + inner_word + close_paren + close_paren)
MOhI_clause << Group(MOhI_pre + MOhI_post)
MOhI_post << Group(post_clause)
MOhI_pre << Group(pre_clause + MOhI + Optional(spaces))
NA << Group(NA_word_pre + inner_word + close_paren + close_paren)
NA_clause << Group(NA_pre + NA_post)
NA_post << Group(post_clause)
NA_pre << Group(pre_clause + NA + Optional(spaces))
NAI << Group(NAI_word_pre + inner_word + close_paren + close_paren)
NAI_clause << Group(NAI_pre + NAI_post)
NAI_post << Group(post_clause)
NAI_pre << Group(pre_clause + NAI + Optional(spaces))
NAhE << Group(NAhE_word_pre + inner_word + close_paren + close_paren)
NAhE_clause << Group(NAhE_pre + NAhE_post)
NAhE_post << Group(post_clause)
NAhE_pre << Group(pre_clause + NAhE + Optional(spaces))
NAhU << Group(NAhU_word_pre + inner_word + close_paren + close_paren)
NAhU_clause << Group(NAhU_pre + NAhU_post)
NAhU_post << Group(post_clause)
NAhU_pre << Group(pre_clause + NAhU + Optional(spaces))
NIhE << Group(NIhE_word_pre + inner_word + close_paren + close_paren)
NIhE_clause << Group(NIhE_pre + NIhE_post)
NIhE_post << Group(post_clause)
NIhE_pre << Group(pre_clause + NIhE + Optional(spaces))
NIhO << Group(NIhO_word_pre + inner_word + close_paren + close_paren)
NIhO_clause << Group(ZeroOrMore(sentence_sa) + NIhO_pre + NIhO_post)
NIhO_post << Group(ZeroOrMore(su_clause) + post_clause)
NIhO_pre << Group(pre_clause + NIhO + Optional(spaces))
NOI << Group(NOI_word_pre + inner_word + close_paren + close_paren)
NOI_clause << Group(NOI_pre + NOI_post)
NOI_post << Group(post_clause)
NOI_pre << Group(pre_clause + NOI + Optional(spaces))
NU << Group(NU_word_pre + inner_word + close_paren + close_paren)
NU_clause << Group(NU_pre + NU_post)
NU_post << Group(post_clause)
NU_pre << Group(pre_clause + NU + Optional(spaces))
NUhA << Group(NUhA_word_pre + inner_word + close_paren + close_paren)
NUhA_clause << Group(NUhA_pre + NUhA_post)
NUhA_post << Group(post_clause)
NUhA_pre << Group(pre_clause + NUhA + Optional(spaces))
NUhI << Group(NUhI_word_pre + inner_word + close_paren + close_paren)
NUhI_clause << Group(NUhI_pre + NUhI_post)
NUhI_post << Group(post_clause)
NUhI_pre << Group(pre_clause + NUhI + Optional(spaces))
NUhU << Group(NUhU_word_pre + inner_word + close_paren + close_paren)
NUhU_clause << Group(NUhU_pre + NUhU_post)
NUhU_post << Group(post_clause)
NUhU_pre << Group(pre_clause + NUhU + Optional(spaces))
PA << Group(PA_word_pre + inner_word + close_paren + close_paren)
PA_clause << Group(PA_pre + PA_post)
PA_post << Group(post_clause)
PA_pre << Group(pre_clause + PA + Optional(spaces))
PEhE << Group(PEhE_word_pre + inner_word + close_paren + close_paren)
PEhE_clause << Group(PEhE_pre + PEhE_post)
PEhE_post << Group(post_clause)
PEhE_pre << Group(pre_clause + PEhE + Optional(spaces))
PEhO << Group(PEhO_word_pre + inner_word + close_paren + close_paren)
PEhO_clause << Group(PEhO_pre + PEhO_post)
PEhO_post << Group(post_clause)
PEhO_pre << Group(pre_clause + PEhO + Optional(spaces))
PU << Group(PU_word_pre + inner_word + close_paren + close_paren)
PU_clause << Group(PU_pre + PU_post)
PU_post << Group(post_clause)
PU_pre << Group(pre_clause + PU + Optional(spaces))
RAhO << Group(RAhO_word_pre + inner_word + close_paren + close_paren)
RAhO_clause << Group(RAhO_pre + RAhO_post)
RAhO_post << Group(post_clause)
RAhO_pre << Group(pre_clause + RAhO + Optional(spaces))
ROI << Group(ROI_word_pre + inner_word + close_paren + close_paren)
ROI_clause << Group(ROI_pre + ROI_post)
ROI_post << Group(post_clause)
ROI_pre << Group(pre_clause + ROI + Optional(spaces))
SA << Group(SA_word_pre + inner_word + close_paren + close_paren)
SA_clause << Group(SA_pre + SA_post)
SA_post << Group(Optional(spaces))
SA_pre << Group(pre_clause + SA + Optional(spaces))
SE << Group(SE_word_pre + inner_word + close_paren + close_paren)
SE_clause << Group(SE_pre + SE_post)
SE_post << Group(post_clause)
SE_pre << Group(pre_clause + SE + Optional(spaces))
SEI << Group(SEI_word_pre + inner_word + close_paren + close_paren)
SEI_clause << Group(SEI_pre + SEI_post)
SEI_post << Group(post_clause)
SEI_pre << Group(pre_clause + SEI + Optional(spaces))
SEhU << Group(SEhU_word_pre + inner_word + close_paren + close_paren)
SEhU_clause << Group(SEhU_pre + SEhU_post)
SEhU_post << Group(post_clause)
SEhU_pre << Group(pre_clause + SEhU + Optional(spaces))
SI << Group(SI_word_pre + inner_word + close_paren + close_paren)
SI_clause << Group(Optional(spaces) + SI + Optional(spaces))
SOI << Group(SOI_word_pre + inner_word + close_paren + close_paren)
SOI_clause << Group(SOI_pre + SOI_post)
SOI_post << Group(post_clause)
SOI_pre << Group(pre_clause + SOI + Optional(spaces))
SU << Group(SU_word_pre + inner_word + close_paren + close_paren)
SU_clause << Group(SU_pre + SU_post)
SU_post << Group(post_clause)
SU_pre << Group(pre_clause + SU + Optional(spaces))
TAhE << Group(TAhE_word_pre + inner_word + close_paren + close_paren)
TAhE_clause << Group(TAhE_pre + TAhE_post)
TAhE_post << Group(post_clause)
TAhE_pre << Group(pre_clause + TAhE + Optional(spaces))
TEI << Group(TEI_word_pre + inner_word + close_paren + close_paren)
TEI_clause << Group(TEI_pre + TEI_post)
TEI_post << Group(post_clause)
TEI_pre << Group(pre_clause + TEI + Optional(spaces))
TEhU << Group(TEhU_word_pre + inner_word + close_paren + close_paren)
TEhU_clause << Group(TEhU_pre + TEhU_post)
TEhU_post << Group(post_clause)
TEhU_pre << Group(pre_clause + TEhU + Optional(spaces))
TO << Group(TO_word_pre + inner_word + close_paren + close_paren)
TO_clause << Group(TO_pre + TO_post)
TO_post << Group(post_clause)
TO_pre << Group(pre_clause + TO + Optional(spaces))
TOI << Group(TOI_word_pre + inner_word + close_paren + close_paren)
TOI_clause << Group(TOI_pre + TOI_post)
TOI_post << Group(post_clause)
TOI_pre << Group(pre_clause + TOI + Optional(spaces))
TUhE << Group(TUhE_word_pre + inner_word + close_paren + close_paren)
TUhE_clause << Group(TUhE_pre + TUhE_post)
TUhE_post << Group(ZeroOrMore(su_clause) + post_clause)
TUhE_pre << Group(pre_clause + TUhE + Optional(spaces))
TUhU << Group(TUhU_word_pre + inner_word + close_paren + close_paren)
TUhU_clause << Group(TUhU_pre + TUhU_post)
TUhU_post << Group(post_clause)
TUhU_pre << Group(pre_clause + TUhU + Optional(spaces))
UI << Group(UI_word_pre + inner_word + close_paren + close_paren)
UI_clause << Group(UI_pre + UI_post)
UI_post << Group(post_clause)
UI_pre << Group(pre_clause + UI + Optional(spaces))
VA << Group(VA_word_pre + inner_word + close_paren + close_paren)
VA_clause << Group(VA_pre + VA_post)
VA_post << Group(post_clause)
VA_pre << Group(pre_clause + VA + Optional(spaces))
VAU << Group(VAU_word_pre + inner_word + close_paren + close_paren)
VAU_clause << Group(VAU_pre + VAU_post)
VAU_post << Group(post_clause)
VAU_pre << Group(pre_clause + VAU + Optional(spaces))
VEI << Group(VEI_word_pre + inner_word + close_paren + close_paren)
VEI_clause << Group(VEI_pre + VEI_post)
VEI_post << Group(post_clause)
VEI_pre << Group(pre_clause + VEI + Optional(spaces))
VEhA << Group(VEhA_word_pre + inner_word + close_paren + close_paren)
VEhA_clause << Group(VEhA_pre + VEhA_post)
VEhA_post << Group(post_clause)
VEhA_pre << Group(pre_clause + VEhA + Optional(spaces))
VEhO << Group(VEhO_word_pre + inner_word + close_paren + close_paren)
VEhO_clause << Group(VEhO_pre + VEhO_post)
VEhO_post << Group(post_clause)
VEhO_pre << Group(pre_clause + VEhO + Optional(spaces))
VIhA << Group(VIhA_word_pre + inner_word + close_paren + close_paren)
VIhA_clause << Group(VIhA_pre + VIhA_post)
VIhA_post << Group(post_clause)
VIhA_pre << Group(pre_clause + VIhA + Optional(spaces))
VUhO << Group(VUhO_word_pre + inner_word + close_paren + close_paren)
VUhO_clause << Group(VUhO_pre + VUhO_post)
VUhO_post << Group(post_clause)
VUhO_pre << Group(pre_clause + VUhO + Optional(spaces))
VUhU << Group(VUhU_word_pre + inner_word + close_paren + close_paren)
VUhU_clause << Group(VUhU_pre + VUhU_post)
VUhU_post << Group(post_clause)
VUhU_pre << Group(pre_clause + VUhU + Optional(spaces))
XI << Group(XI_word_pre + inner_word + close_paren + close_paren)
XI_clause << Group(XI_pre + XI_post)
XI_post << Group(post_clause)
XI_pre << Group(pre_clause + XI + Optional(spaces))
ZAhO << Group(ZAhO_word_pre + inner_word + close_paren + close_paren)
ZAhO_clause << Group(ZAhO_pre + ZAhO_post)
ZAhO_post << Group(post_clause)
ZAhO_pre << Group(pre_clause + ZAhO + Optional(spaces))
ZEI << Group(ZEI_word_pre + inner_word + close_paren + close_paren)
ZEI_clause << Group(ZEI_pre + ZEI_post)
ZEI_post << Group(Optional(spaces))
ZEI_pre << Group(pre_clause + ZEI + Optional(spaces))
ZEhA << Group(ZEhA_word_pre + inner_word + close_paren + close_paren)
ZEhA_clause << Group(ZEhA_pre + ZEhA_post)
ZEhA_post << Group(post_clause)
ZEhA_pre << Group(pre_clause + ZEhA + Optional(spaces))
ZI << Group(ZI_word_pre + inner_word + close_paren + close_paren)
ZI_clause << Group(ZI_pre + ZI_post)
ZI_post << Group(post_clause)
ZI_pre << Group(pre_clause + ZI + Optional(spaces))
ZIhE << Group(ZIhE_word_pre + inner_word + close_paren + close_paren)
ZIhE_clause << Group(ZIhE_pre + ZIhE_post)
ZIhE_post << Group(post_clause)
ZIhE_pre << Group(pre_clause + ZIhE + Optional(spaces))
ZO << Group(ZO_word_pre + inner_word + close_paren + close_paren)
ZO_clause << Group(ZO_pre + ZO_post)
ZO_post << Group(post_clause)
ZO_pre << Group(pre_clause + ZO + Optional(spaces) + any_word + Optional(spaces))
ZOI << Group(ZOI_word_pre + inner_word + close_paren + close_paren)
ZOI_clause << Group(ZOI_pre + ZOI_post)
ZOI_post << Group(post_clause)
ZOI_pre << Group(pre_clause + ZOI + Optional(spaces) + zoi_open + ZeroOrMore(zoi_word) + zoi_close + Optional(spaces))
ZOhU << Group(ZOhU_word_pre + inner_word + close_paren + close_paren)
ZOhU_clause << Group(ZOhU_pre + ZOhU_post)
ZOhU_post << Group(post_clause)
ZOhU_pre << Group(pre_clause + ZOhU + Optional(spaces))
any_word << Group(any_word_pre + inner_word + close_paren + Optional(spaces))
any_word_SA_handling << Group(BRIVLA_pre | known_cmavo_SA | ~known_cmavo_pre + CMAVO_pre | CMENE_pre)
bridi_tail << Group(bridi_tail_1 + Optional(gihek + Optional(stag) + KE_clause + ZeroOrMore(free) + bridi_tail + Optional(KEhE_clause) + ZeroOrMore(free) + tail_terms))
bridi_tail_1 << Group(bridi_tail_2 + ZeroOrMore(gihek + ~(Optional(stag) + BO_clause) + ~(Optional(stag) + KE_clause) + ZeroOrMore(free) + bridi_tail_2 + tail_terms))
bridi_tail_2 << Group(bridi_tail_3 + Optional(gihek + Optional(stag) + BO_clause + ZeroOrMore(free) + bridi_tail_2 + tail_terms))
bridi_tail_3 << Group(selbri + tail_terms | gek_sentence)
bridi_tail_sa << Group(bridi_tail_start + ZeroOrMore(term | ~bridi_tail_start + (sa_word | SA_clause + ~bridi_tail_start)) + SA_clause + FollowedBy(bridi_tail))
bridi_tail_start << Group(ME_clause | NUhA_clause | NU_clause | NA_clause + ~KU_clause | NAhE_clause + ~BO_clause | selbri | tag + bridi_tail_start | KE_clause + bridi_tail_start | bridi_tail)
bu_clause << Group(pre_clause + bu_clause_no_pre)
bu_clause_no_pre << Group(pre_zei_bu + ZeroOrMore(Optional(bu_tail) + zei_tail) + bu_tail + post_clause)
bu_tail << Group(OneOrMore(BU_clause))
cehe_sa << Group(CEhE_clause + ZeroOrMore(~CEhE_clause + (sa_word | SA_clause + ~CEhE_clause)) + SA_clause)
ek << Group(Optional(NA_clause) + Optional(SE_clause) + A_clause + Optional(NAI_clause))
erasable_clause << Group(bu_clause_no_pre + ~ZEI_clause + ~BU_clause | zei_clause_no_pre + ~ZEI_clause + ~BU_clause)
faho_clause << Group(Optional(FAhO_clause + dot_star))
fore_operands << Group(OneOrMore(mex_2))
fragment << Group(prenex | terms + Optional(VAU_clause) + ZeroOrMore(free) | ek + ZeroOrMore(free) | gihek + ZeroOrMore(free) | quantifier | NA_clause + ~JA_clause + ZeroOrMore(free) | relative_clauses | links | linkargs)
free << Group(SEI_clause + ZeroOrMore(free) + Optional(terms + Optional(CU_clause) + ZeroOrMore(free)) + selbri + Optional(SEhU_clause) | SOI_clause + ZeroOrMore(free) + sumti + Optional(sumti) + Optional(SEhU_clause) | vocative + Optional(relative_clauses) + selbri + Optional(relative_clauses) + Optional(DOhU_clause) | vocative + Optional(relative_clauses) + OneOrMore(CMENE_clause) + ZeroOrMore(free) + Optional(relative_clauses) + Optional(DOhU_clause) | vocative + Optional(sumti) + Optional(DOhU_clause) | (number | lerfu_string) + MAI_clause | TO_clause + text + Optional(TOI_clause) | xi_clause)
gek << Group(Optional(SE_clause) + GA_clause + Optional(NAI_clause) + ZeroOrMore(free) | joik + GI_clause + ZeroOrMore(free) | stag + gik)
gek_sentence << Group(gek + subsentence + gik + subsentence + tail_terms | Optional(tag) + KE_clause + ZeroOrMore(free) + gek_sentence + Optional(KEhE_clause) + ZeroOrMore(free) | NA_clause + ZeroOrMore(free) + gek_sentence)
gek_termset << Group(gek + terms_gik_terms)
gihek << Group(ZeroOrMore(gihek_sa) + gihek_1)
gihek_1 << Group(Optional(NA_clause) + Optional(SE_clause) + GIhA_clause + Optional(NAI_clause))
gihek_sa << Group(gihek_1 + ZeroOrMore(~gihek_1 + (sa_word | SA_clause + ~gihek_1)) + SA_clause + FollowedBy(gihek))
gik << Group(GI_clause + Optional(NAI_clause) + ZeroOrMore(free))
guhek << Group(Optional(SE_clause) + GUhA_clause + Optional(NAI_clause) + ZeroOrMore(free))
indicator << Group(((UI_clause | CAI_clause) + Optional(NAI_clause) | DAhO_clause | FUhO_clause) + ~BU_clause)
indicators << Group(Optional(FUhE_clause) + OneOrMore(indicator))
inner_word << Group(space_char + OneOrMore(~equals_char + ~space_char + Regex('.')) + equals_char + open_paren + inner_word + close_paren + Optional(inner_word) | inner_word2)
inner_word2 << Group(~close_paren_char + Regex('.') + inner_word2 | ~close_paren_char + Regex('.') + FollowedBy(space_char))
interval << Group(Optional(SE_clause) + BIhI_clause + Optional(NAI_clause))
interval_property << Group(number + ROI_clause + Optional(NAI_clause) | TAhE_clause + Optional(NAI_clause) | ZAhO_clause + Optional(NAI_clause))
intro_null << Group(Optional(spaces) + ZeroOrMore(su_clause) + intro_si_clause)
intro_si_clause << Group(Optional(si_clause) + ZeroOrMore(SI_clause))
jek << Group(Optional(NA_clause) + Optional(SE_clause) + JA_clause + Optional(NAI_clause))
joik << Group(Optional(SE_clause) + JOI_clause + Optional(NAI_clause) | interval | GAhO_clause + interval + GAhO_clause)
joik_ek << Group(ZeroOrMore(joik_ek_sa) + joik_ek_1)
joik_ek_1 << Group(joik + ZeroOrMore(free) | ek + ZeroOrMore(free))
joik_ek_sa << Group(joik_ek_1 + ZeroOrMore(~joik_ek_1 + (sa_word | SA_clause + ~joik_ek_1)) + SA_clause + FollowedBy(joik_ek))
joik_jek << Group(joik + ZeroOrMore(free) | jek + ZeroOrMore(free))
known_cmavo_SA << Group(A_pre | BAI_pre | BAhE_pre | BE_pre | BEI_pre | BEhO_pre | BIhE_pre | BIhI_pre | BO_pre | BOI_pre | BU_pre | BY_pre | CAI_pre | CAhA_pre | CEI_pre | CEhE_pre | CO_pre | COI_pre | CU_pre | CUhE_pre | DAhO_pre | DOI_pre | DOhU_pre | FA_pre | FAhA_pre | FEhE_pre | FEhU_pre | FIhO_pre | FOI_pre | FUhA_pre | FUhE_pre | FUhO_pre | GA_pre | GAhO_pre | GEhU_pre | GI_pre | GIhA_pre | GOI_pre | GOhA_pre | GUhA_pre | I_pre | JA_pre | JAI_pre | JOI_pre | JOhI_pre | KE_pre | KEI_pre | KEhE_pre | KI_pre | KOhA_pre | KU_pre | KUhE_pre | KUhO_pre | LA_pre | LAU_pre | LAhE_pre | LE_pre | LEhU_pre | LI_pre | LIhU_pre | LOhO_pre | LOhU_pre | LU_pre | LUhU_pre | MAI_pre | MAhO_pre | ME_pre | MEhU_pre | MOI_pre | MOhE_pre | MOhI_pre | NA_pre | NAI_pre | NAhE_pre | NAhU_pre | NIhE_pre | NIhO_pre | NOI_pre | NU_pre | NUhA_pre | NUhI_pre | NUhU_pre | PA_pre | PEhE_pre | PEhO_pre | PU_pre | RAhO_pre | ROI_pre | SA_pre | SE_pre | SEI_pre | SEhU_pre | SI_clause | SOI_pre | SU_pre | TAhE_pre | TEI_pre | TEhU_pre | TO_pre | TOI_pre | TUhE_pre | TUhU_pre | UI_pre | VA_pre | VAU_pre | VEI_pre | VEhA_pre | VEhO_pre | VIhA_pre | VUhO_pre | VUhU_pre | XI_pre | ZAhO_pre | ZEI_pre | ZEhA_pre | ZI_pre | ZIhE_pre | ZO_pre | ZOI_pre | ZOhU_pre)
lerfu_string << Group(lerfu_word + ZeroOrMore(PA_clause | lerfu_word))
lerfu_word << Group(BY_clause | LAU_clause + lerfu_word | TEI_clause + lerfu_string + FOI_clause)
li_clause << Group(LI_clause + ZeroOrMore(free) + mex + Optional(LOhO_clause) + ZeroOrMore(free))
linkargs << Group(ZeroOrMore(linkargs_sa) + linkargs_1)
linkargs_1 << Group(BE_clause + ZeroOrMore(free) + term + Optional(links) + Optional(BEhO_clause) + ZeroOrMore(free))
linkargs_sa << Group(linkargs_start + ZeroOrMore(~linkargs_start + (sa_word | SA_clause + ~linkargs_start)) + SA_clause + FollowedBy(linkargs_1))
linkargs_start << Group(BE_clause)
links << Group(ZeroOrMore(links_sa) + links_1)
links_1 << Group(BEI_clause + ZeroOrMore(free) + term + Optional(links))
links_sa << Group(links_start + ZeroOrMore(~links_start + (sa_word | SA_clause + ~links_start)) + SA_clause + FollowedBy(links_1))
links_start << Group(BEI_clause)
mex << Group(ZeroOrMore(mex_sa) + mex_0)
mex_0 << Group(mex_1 + ZeroOrMore(operator + mex_1) | rp_clause)
mex_1 << Group(mex_2 + Optional(BIhE_clause + ZeroOrMore(free) + operator + mex_1))
mex_2 << Group(operand | mex_forethought)
mex_forethought << Group(Optional(PEhO_clause) + ZeroOrMore(free) + operator + fore_operands + Optional(KUhE_clause) + ZeroOrMore(free))
mex_operator << Group(SE_clause + ZeroOrMore(free) + mex_operator | NAhE_clause + ZeroOrMore(free) + mex_operator | MAhO_clause + ZeroOrMore(free) + mex + Optional(TEhU_clause) + ZeroOrMore(free) | NAhU_clause + ZeroOrMore(free) + selbri + Optional(TEhU_clause) + ZeroOrMore(free) | VUhU_clause + ZeroOrMore(free))
mex_sa << Group(mex_start + ZeroOrMore(~mex_start + (sa_word | SA_clause + ~mex_start)) + SA_clause + FollowedBy(mex_0))
mex_start << Group(FUhA_clause | PEhO_clause | operand_start)
number << Group(PA_clause + ZeroOrMore(PA_clause | lerfu_word))
operand << Group(ZeroOrMore(operand_sa) + operand_0)
operand_0 << Group(operand_1 + Optional(joik_ek + Optional(stag) + KE_clause + ZeroOrMore(free) + operand + Optional(KEhE_clause) + ZeroOrMore(free)))
operand_1 << Group(operand_2 + ZeroOrMore(joik_ek + operand_2))
operand_2 << Group(operand_3 + Optional(joik_ek + Optional(stag) + BO_clause + ZeroOrMore(free) + operand_2))
operand_3 << Group(quantifier | lerfu_string + ~MOI_clause + Optional(BOI_clause) + ZeroOrMore(free) | NIhE_clause + ZeroOrMore(free) + selbri + Optional(TEhU_clause) + ZeroOrMore(free) | MOhE_clause + ZeroOrMore(free) + sumti + Optional(TEhU_clause) + ZeroOrMore(free) | JOhI_clause + ZeroOrMore(free) + OneOrMore(mex_2) + Optional(TEhU_clause) + ZeroOrMore(free) | gek + operand + gik + operand_3 | (LAhE_clause + ZeroOrMore(free) | NAhE_clause + BO_clause + ZeroOrMore(free)) + operand + Optional(LUhU_clause) + ZeroOrMore(free))
operand_sa << Group(operand_start + ZeroOrMore(~operand_start + (sa_word | SA_clause + ~operand_start)) + SA_clause + FollowedBy(operand_0))
operand_start << Group(quantifier | lerfu_word | NIhE_clause | MOhE_clause | JOhI_clause | gek | LAhE_clause | NAhE_clause)
operator << Group(ZeroOrMore(operator_sa) + operator_0)
operator_0 << Group(operator_1 + ZeroOrMore(joik_jek + operator_1 | joik + Optional(stag) + KE_clause + ZeroOrMore(free) + operator + Optional(KEhE_clause) + ZeroOrMore(free)))
operator_1 << Group(operator_2 | guhek + operator_1 + gik + operator_2 | operator_2 + (jek | joik) + Optional(stag) + BO_clause + ZeroOrMore(free) + operator_1)
operator_2 << Group(mex_operator | KE_clause + ZeroOrMore(free) + operator + Optional(KEhE_clause) + ZeroOrMore(free))
operator_sa << Group(operator_start + ZeroOrMore(~operator_start + (sa_word | SA_clause + ~operator_start)) + SA_clause + FollowedBy(operator_0))
operator_start << Group(guhek | KE_clause | Optional(SE_clause) + NAhE_clause | Optional(SE_clause) + MAhO_clause | Optional(SE_clause) + VUhU_clause)
paragraph << Group((statement | fragment) + ZeroOrMore(I_clause + ~jek + ~joik + ~joik_jek + ZeroOrMore(free) + Optional(statement | fragment)))
paragraphs << Group(paragraph + Optional(OneOrMore(NIhO_clause) + ZeroOrMore(free) + ZeroOrMore(su_clause) + paragraphs))
pehe_sa << Group(PEhE_clause + ZeroOrMore(~PEhE_clause + (sa_word | SA_clause + ~PEhE_clause)) + SA_clause)
post_clause << Group(Optional(spaces) + Optional(si_clause) + ~ZEI_clause + ~BU_clause + ZeroOrMore(indicators))
pre_clause << Group(Optional(BAhE_clause))
pre_zei_bu << Group(~BU_clause + ~ZEI_clause + ~SI_clause + ~SA_clause + ~SU_clause + ~FAhO_clause + any_word_SA_handling + Optional(si_clause))
prenex << Group(terms + ZOhU_clause + ZeroOrMore(free))
quantifier << Group(number + ~MOI_clause + Optional(BOI_clause) + ZeroOrMore(free) | VEI_clause + ZeroOrMore(free) + mex + Optional(VEhO_clause) + ZeroOrMore(free))
relative_clause << Group(ZeroOrMore(relative_clause_sa) + relative_clause_1)
relative_clause_1 << Group(GOI_clause + ZeroOrMore(free) + term + Optional(GEhU_clause) + ZeroOrMore(free) | NOI_clause + ZeroOrMore(free) + subsentence + Optional(KUhO_clause) + ZeroOrMore(free))
relative_clause_sa << Group(relative_clause_start + ZeroOrMore(~relative_clause_start + (sa_word | SA_clause + ~relative_clause_start)) + SA_clause + FollowedBy(relative_clause_1))
relative_clause_start << Group(GOI_clause | NOI_clause)
relative_clauses << Group(relative_clause + ZeroOrMore(ZIhE_clause + ZeroOrMore(free) + relative_clause))
rp_clause << Group(FUhA_clause + ZeroOrMore(free) + rp_expression)
rp_expression << Group(operand + rp_expression_tail)
rp_expression_tail << Group(Optional(rp_expression + operator + rp_expression_tail))
sa_word << Group(pre_zei_bu)
selbri << Group(Optional(tag) + selbri_1)
selbri_1 << Group(selbri_2 | NA_clause + ZeroOrMore(free) + selbri)
selbri_2 << Group(selbri_3 + Optional(CO_clause + ZeroOrMore(free) + selbri_2))
selbri_3 << Group(OneOrMore(selbri_4))
selbri_4 << Group(selbri_5 + ZeroOrMore(joik_jek + selbri_5 | joik + Optional(stag) + KE_clause + ZeroOrMore(free) + selbri_3 + Optional(KEhE_clause) + ZeroOrMore(free)))
selbri_5 << Group(selbri_6 + Optional((jek | joik) + Optional(stag) + BO_clause + ZeroOrMore(free) + selbri_5))
selbri_6 << Group(tanru_unit + Optional(BO_clause + ZeroOrMore(free) + selbri_6) | Optional(NAhE_clause) + ZeroOrMore(free) + guhek + selbri + gik + selbri_6)
sentence << Group(Optional(terms + ZeroOrMore(bridi_tail_sa) + Optional(CU_clause) + ZeroOrMore(free)) + ZeroOrMore(bridi_tail_sa) + bridi_tail)
sentence_sa << Group(sentence_start + ZeroOrMore(~sentence_start + (sa_word | SA_clause + ~sentence_start)) + SA_clause + FollowedBy(text_1))
sentence_start << Group(I_pre | NIhO_pre)
si_clause << Group(OneOrMore((erasable_clause | si_word | SA_clause) + Optional(si_clause) + SI_clause))
si_word << Group(pre_zei_bu)
simple_tense_modal << Group(Optional(NAhE_clause) + Optional(SE_clause) + BAI_clause + Optional(NAI_clause) + Optional(KI_clause) | Optional(NAhE_clause) + ((time + Optional(space) | space + Optional(time)) + CAhA_clause | time + Optional(space) | space + Optional(time) | CAhA_clause) + Optional(KI_clause) | KI_clause | CUhE_clause)
space << Group(VA_clause + ZeroOrMore(space_offset) + Optional(space_interval) + Optional(MOhI_clause + space_offset) | Optional(VA_clause) + OneOrMore(space_offset) + Optional(space_interval) + Optional(MOhI_clause + space_offset) | Optional(VA_clause) + ZeroOrMore(space_offset) + space_interval + Optional(MOhI_clause + space_offset) | Optional(VA_clause) + ZeroOrMore(space_offset) + Optional(space_interval) + MOhI_clause + space_offset)
space_int_props << Group(OneOrMore(FEhE_clause + interval_property))
space_interval << Group((VEhA_clause | VIhA_clause | VEhA_clause + VIhA_clause) + Optional(FAhA_clause + Optional(NAI_clause)) + space_int_props | (VEhA_clause | VIhA_clause | VEhA_clause + VIhA_clause) + Optional(FAhA_clause + Optional(NAI_clause)) | space_int_props)
space_offset << Group(FAhA_clause + Optional(NAI_clause) + Optional(VA_clause))
spaces << Group(ZeroOrMore(spaces_pre + inner_word + close_paren))
stag << Group(simple_tense_modal + ZeroOrMore((jek | joik) + simple_tense_modal) | tense_modal + ZeroOrMore(joik_jek + tense_modal))
statement << Group(statement_1 | prenex + statement)
statement_1 << Group(statement_2 + ZeroOrMore(I_clause + joik_jek + Optional(statement_2)))
statement_2 << Group(statement_3 + Optional(I_clause + Optional(jek | joik) + Optional(stag) + BO_clause + ZeroOrMore(free) + statement_2) | statement_3 + Optional(I_clause + Optional(jek | joik) + Optional(stag) + BO_clause + ZeroOrMore(free)))
statement_3 << Group(sentence | Optional(tag) + TUhE_clause + ZeroOrMore(free) + text_1 + Optional(TUhU_clause) + ZeroOrMore(free))
su_clause << Group(ZeroOrMore(erasable_clause | su_word) + SU_clause)
su_word << Group(~NIhO_clause + ~LU_clause + ~TUhE_clause + ~TO_clause + ~SU_clause + ~FAhO_clause + any_word_SA_handling)
subsentence << Group(sentence | prenex + subsentence)
sumti << Group(sumti_1 + Optional(VUhO_clause + ZeroOrMore(free) + relative_clauses))
sumti_1 << Group(sumti_2 + Optional(joik_ek + Optional(stag) + KE_clause + ZeroOrMore(free) + sumti + Optional(KEhE_clause) + ZeroOrMore(free)))
sumti_2 << Group(sumti_3 + ZeroOrMore(joik_ek + sumti_3))
sumti_3 << Group(sumti_4 + Optional(joik_ek + Optional(stag) + BO_clause + ZeroOrMore(free) + sumti_3))
sumti_4 << Group(sumti_5 | gek + sumti + gik + sumti_4)
sumti_5 << Group(Optional(quantifier) + sumti_6 + Optional(relative_clauses) | quantifier + selbri + Optional(KU_clause) + ZeroOrMore(free) + Optional(relative_clauses))
sumti_6 << Group(ZO_clause + ZeroOrMore(free) | ZOI_clause + ZeroOrMore(free) | LOhU_clause + ZeroOrMore(free) | lerfu_string + ~MOI_clause + Optional(BOI_clause) + ZeroOrMore(free) | LU_clause + text + Optional(LIhU_clause) + ZeroOrMore(free) | (LAhE_clause + ZeroOrMore(free) | NAhE_clause + BO_clause + ZeroOrMore(free)) + Optional(relative_clauses) + sumti + Optional(LUhU_clause) + ZeroOrMore(free) | KOhA_clause + ZeroOrMore(free) | LA_clause + ZeroOrMore(free) + Optional(relative_clauses) + OneOrMore(CMENE_clause) + ZeroOrMore(free) | (LA_clause | LE_clause) + ZeroOrMore(free) + sumti_tail + Optional(KU_clause) + ZeroOrMore(free) | li_clause)
sumti_tail << Group(Optional(sumti_6 + Optional(relative_clauses)) + sumti_tail_1 | relative_clauses + sumti_tail_1)
sumti_tail_1 << Group(selbri + Optional(relative_clauses) | quantifier + selbri + Optional(relative_clauses) | quantifier + sumti)
tag << Group(tense_modal + ZeroOrMore(joik_jek + tense_modal))
tail_terms << Group(Optional(terms) + Optional(VAU_clause) + ZeroOrMore(free))
tanru_unit << Group(tanru_unit_1 + ZeroOrMore(CEI_clause + ZeroOrMore(free) + tanru_unit_1))
tanru_unit_1 << Group(tanru_unit_2 + Optional(linkargs))
tanru_unit_2 << Group(BRIVLA_clause + ZeroOrMore(free) | GOhA_clause + Optional(RAhO_clause) + ZeroOrMore(free) | KE_clause + ZeroOrMore(free) + selbri_3 + Optional(KEhE_clause) + ZeroOrMore(free) | ME_clause + ZeroOrMore(free) + (sumti | lerfu_string) + Optional(MEhU_clause) + ZeroOrMore(free) + Optional(MOI_clause) + ZeroOrMore(free) | (number | lerfu_string) + MOI_clause + ZeroOrMore(free) | NUhA_clause + ZeroOrMore(free) + mex_operator | SE_clause + ZeroOrMore(free) + tanru_unit_2 | JAI_clause + ZeroOrMore(free) + Optional(tag) + tanru_unit_2 | NAhE_clause + ZeroOrMore(free) + tanru_unit_2 | NU_clause + Optional(NAI_clause) + ZeroOrMore(free) + ZeroOrMore(joik_jek + NU_clause + Optional(NAI_clause) + ZeroOrMore(free)) + subsentence + Optional(KEI_clause) + ZeroOrMore(free))
tense_modal << Group(simple_tense_modal + ZeroOrMore(free) | FIhO_clause + ZeroOrMore(free) + selbri + Optional(FEhU_clause) + ZeroOrMore(free))
term << Group(ZeroOrMore(term_sa) + term_1)
term_1 << Group(sumti | ~gek + (tag | FA_clause + ZeroOrMore(free)) + (sumti | Optional(KU_clause) + ZeroOrMore(free)) | termset | NA_clause + KU_clause + ZeroOrMore(free))
term_sa << Group(term_start + ZeroOrMore(~term_start + (sa_word | SA_clause + ~term_start)) + SA_clause + FollowedBy(term_1))
term_start << Group(term_1 | LA_clause | LE_clause | LI_clause | LU_clause | LAhE_clause | quantifier + term_start | gek + sumti + gik | FA_clause | tag + term_start)
terms << Group(OneOrMore(terms_1))
terms_1 << Group(terms_2 + ZeroOrMore(ZeroOrMore(pehe_sa) + PEhE_clause + ZeroOrMore(free) + joik_jek + terms_2))
terms_2 << Group(term + ZeroOrMore(ZeroOrMore(cehe_sa) + CEhE_clause + ZeroOrMore(free) + term))
terms_gik_terms << Group(term + (gik | terms_gik_terms) + term)
termset << Group(gek_termset | NUhI_clause + ZeroOrMore(free) + gek + terms + Optional(NUhU_clause) + ZeroOrMore(free) + gik + terms + Optional(NUhU_clause) + ZeroOrMore(free) | NUhI_clause + ZeroOrMore(free) + terms + Optional(NUhU_clause) + ZeroOrMore(free))
text << Group(intro_null + ZeroOrMore(NAI_clause) + text_part_2 + Optional(~text_1 + joik_jek) + Optional(text_1) + faho_clause + Optional(EOF))
text_1 << Group(I_clause + Optional(jek | joik) + Optional(Optional(stag) + BO_clause) + ZeroOrMore(free) + Optional(text_1) | OneOrMore(NIhO_clause) + ZeroOrMore(free) + ZeroOrMore(su_clause) + Optional(paragraphs) | paragraphs)
text_part_2 << Group((OneOrMore(CMENE_clause) | Optional(indicators)) + ZeroOrMore(free))
time << Group(ZI_clause + ZeroOrMore(time_offset) + Optional(ZEhA_clause + Optional(PU_clause + Optional(NAI_clause))) + ZeroOrMore(interval_property) | Optional(ZI_clause) + OneOrMore(time_offset) + Optional(ZEhA_clause + Optional(PU_clause + Optional(NAI_clause))) + ZeroOrMore(interval_property) | Optional(ZI_clause) + ZeroOrMore(time_offset) + ZEhA_clause + Optional(PU_clause + Optional(NAI_clause)) + ZeroOrMore(interval_property) | Optional(ZI_clause) + ZeroOrMore(time_offset) + Optional(ZEhA_clause + Optional(PU_clause + Optional(NAI_clause))) + OneOrMore(interval_property))
time_offset << Group(PU_clause + Optional(NAI_clause) + Optional(ZI_clause))
vocative << Group(ZeroOrMore(COI_clause + Optional(NAI_clause)) + DOI_clause | OneOrMore(COI_clause + Optional(NAI_clause)))
xi_clause << Group(XI_clause + ZeroOrMore(free) + (number | lerfu_string) + Optional(BOI_clause) | XI_clause + ZeroOrMore(free) + VEI_clause + ZeroOrMore(free) + mex + Optional(VEhO_clause))
zei_clause << Group(pre_clause + zei_clause_no_pre)
zei_clause_no_pre << Group(pre_zei_bu + ZeroOrMore(Optional(zei_tail) + bu_tail) + zei_tail + post_clause)
zei_tail << Group(OneOrMore(ZEI_clause + any_word))

