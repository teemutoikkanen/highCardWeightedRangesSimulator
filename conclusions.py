


# 25bb BvB tilanne missä SB:n strategia AI/FOLD. 

# ICMIZER equilibrium strategia olisi: SB shove 39%, BB calls 17.39% 

# ICZMIER ei ilmeisesti ota huomioon paskojen korttien removalia, kun EP-BTN kipannut roskakäsiä. 
# Mallinetaan tilannetta niin, että simuloiitiin 250k jakoa, missä 6 pelaajaa kipannut bottom 81%-rangen. 
# Lopulla pakalla jaettiin aina BB:lle random käsikombinaatio 250000 kertaa.

# Tulos: BB herääkin maksurangella (17.39%) nyt 18,7% ajasta. Erotus on siis 1,7%. Siis BB herää 10% useammin (1,7%/17%) kuin mitä 17% range heräisi ilman removalia.

# Tutkitaan SB:n huonoimpien käsien EV:tä. SB 5 BB 10, antes 8*1. Stackit 249:

# EV_villain_folds = 249+10+8 


# # Q9o: 
# EV_villain_calls = 0.3495*250*2+6
# call_freq = 0.1825
# fold_freq = (1-call_freq)
# EVtot = EV_villain_folds*fold_freq+EV_villain_calls*call_freq
# print(EVtot)

# #Siis T9o olis vielä selvästi voitollinen pusku







# syitä miksi tämä tutkimus ei ole 100% validi:
# *softassa voi olla bugeja
# *en ota huomioon SB:lle jaettujen korttien removalia. tää kyllä onnistuis jos jaksan vielä jatkaa tätä projektia. PAKKO LISÄTÄ; ESIM ICMIZERISSA JO NÄKEE NÄÄ LUVUT; ISOJA EROJA.
# *en ota huomioon miten eri kombojen painoarvot eroavat toisistaan BB:n maksurangessa, korjattavissa. Siis lasken vaan "kuinka usein BB herää maksukädellä", en laske esimerkiksi mitkä kädet heräävät useammin





#######################

#ylemmäs väärät ranget: oikeet:
#shove 44%
# 



#J5s vs 25bb calling range. (EV hero fold eli 0-EV olis 245)
EV_villain_folds = 249+10+8 

hero_equity = 0.3547
EV_villain_calls = hero_equity*250*2+6
call_freq = 0.2594
# call_freq = 0.2620 #icmizer ottaa huomioon oman käden removalin maksu % !
fold_freq = (1 - call_freq)
EVtot = EV_villain_folds*fold_freq+EV_villain_calls*call_freq
print(EVtot)

#TULOS käyttäen call_freq_icmizer=0.262
245.0837
#TULOS ilman oman käden removalia
#ICM EV +0.07
#ICM EV HU +0.07, V calls 26.20%
# SIIS ICM EI OTA PASSIVE REMOVALIA HUOMIOON !! MIKSI ERI TULOS ??


