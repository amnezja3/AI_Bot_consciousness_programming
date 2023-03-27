def whatWho(xSentenceVerbs):
    import coffeeBrain as cf
    meaningBase = cf.coffeePls(False)[3]
    xSentenceVerbs = str(xSentenceVerbs)
    words = xSentenceVerbs.split()

    export = []
    for k in words:
        try: v = meaningBase[k]
        except KeyError: v = '#cz.mowy#UNK' 
        if str(v).startswith('#cz.mowy#czasownik'):
            if str(k).endswith('am') or str(k).endswith('my') or str(k).endswith('ysz') or str(k).endswith('cie')\
                or str(k).endswith('a') or str(k).endswith('si') or str(k).endswith('ał') or str(k).endswith('ił')\
                    or str(k).endswith('iło') or str(k).endswith('ało') or str(k).endswith('iła') or str(k).endswith('ała')\
                        or str(k).endswith('ją') or str(k).endswith('li') or str(k).endswith('ały') or str(k).endswith('yły')\
                            or str(k).endswith('yli') or str(k).endswith('ali') or str(k).endswith('je') or str(k).endswith('rze')\
                                or str(k).endswith('oi') or str(k).endswith('ła') or str(k).endswith('gł') or str(k).endswith('oł')\
                                    or str(k).endswith('oi') or str(k).endswith('oi') or str(k).endswith('ać') or str(k).endswith('esz')\
                                        or str(k).endswith('dzą'):
                if str(k).endswith('am'):
                    export.append([k, '- JA'])
                if str(k).endswith('my'):
                    export.append([k, '- MY'])
                if str(k).endswith('ysz') or str(k).endswith('ać') or str(k).endswith('esz'):
                    export.append([k, '- TY'])
                if str(k).endswith('cie'):
                    export.append([k, '- WY'])
                if str(k).endswith('a') or str(k).endswith('si')\
                    or str(k).endswith('ał') or str(k).endswith('ił')\
                        or str(k).endswith('iło') or str(k).endswith('ało')\
                            or str(k).endswith('iła') or str(k).endswith('ła')\
                                or str(k).endswith('je') or str(k).endswith('rze')\
                                    or str(k).endswith('oi') or str(k).endswith('gł') \
                                        or str(k).endswith('oł'):
                    export.append([k, '- on/ona/ono'])
                    if str(k).endswith('ał') or str(k).endswith('ił') or str(k).endswith('gł'):
                        export.append([k, '- on'])
                        if str(k).endswith('gł') or str(k).endswith('oł'):
                            export.append([k, '- on aspekt dokonany'])
                    if str(k).endswith('iła') or str(k).endswith('ała'):
                        export.append([k, '- ona'])
                    elif str(k).endswith('ła'):
                        export.append([k, '- ona aspekt dokonany'])
                    if str(k).endswith('iło') or str(k).endswith('ało'):
                        export.append([k, '- ono'])
                    if str(k).endswith('je') or str(k).endswith('rze') or str(k).endswith('oi'):
                        export.append([k, '- on/ona/ono aspekt nie dokonany'])
                        if str(k).endswith('uje'):
                            export.append([k, '- on aspekt nie dokonany - strona czynna '])
                if str(k).endswith('ją') or str(k).endswith('li') \
                    or str(k).endswith('ały') or str(k).endswith('yły')\
                        or str(k).endswith('yli') or str(k).endswith('ali') \
                            or str(k).endswith('dzą'):
                    export.append([k, '- oni/one'])
                    if str(k).endswith('ją') :
                        export.append([k, '- oni/one strona zwtorna'])
            if str(k).endswith('ię') or str(k).endswith('ać') or  str(k).endswith('dzi') or str(k).endswith('na')\
                or str(k).endswith('aj') or str(k).endswith('adź') or str(k).endswith('ądź') or str(k).endswith('aż')\
                    or str(k).endswith('edz') or str(k).endswith('eź') or str(k).endswith('by') or str(k).endswith('byś')\
                        or str(k).endswith('by'):
                if str(k).endswith('ię') or str(k).endswith('ać') or  str(k).endswith('dzi') \
                    or str(k).endswith('na'):
                        export.append([k, '- tryby orzekający'])
                if str(k).endswith('aj') or str(k).endswith('adź') or str(k).endswith('ądź')\
                    or str(k).endswith('edz') or str(k).endswith('eź'):
                    export.append([k, '- tryby rozkazujacy'])
                if str(k).endswith('by') or str(k).endswith('byś') or str(k).endswith('by'):
                    export.append([k, '- tryby przypuszczający'])
    return export
# print(JA, MY, TY, WY, ONO, ONE)

"""
przez strony
	czynną [PODMIOT JEST AKTYWNYM WYKONAWCĄ CZYNNOŚCI]
		- Mateusz griluje kiełbaski
			(Mateusz aktywnie wykonuje czynność grilowania)
	bierną [ZMIENIA PODMIOT]
		- Kiełbaski są grilowane przez Mateusza
			(Kiełbaski nie wykonują aktywnie żadnej czynności. Wykonuje ja Mateusz a kiełbaski ją odbierają same pozostając biernym)
	zwrotną [PODMIOT JEST WYKONAWCĄ JAK I ODBIORCĄ CZYNNOŚCI]
		- kiełbaski grilują się
			(stronę zwrotną wskazuje zaimek się) !!!
	- przegląda, jest przeglądany, przygląda się



przez aspekty [INFORMUJĄ O TYM CZY CZYNNOŚĆ TRWA LUB BEDZIE TRWAŁA, ZKOŃCZYŁA SIĘ LUB ZAKOŃCZY W PRZYSZŁOŚCI]
	dokonany [INFORMUJĄ ŻE DANA CZYNNOŚĆ ZOSTAŁA DOKONANA LUB ZAKOŃCZY SIĘ W PRZYSZŁOŚCI I MOŻNA PRZEWIDZIEĆ JEJ REZULATA]
		- umyje
		- obierze
		- pokroi
		- ugotuje
		- zje
			(rozpoznie cz. dok. ułatwia dodnanie do nich zwrotu RAZ A DOBRZE, jeżeli wyrażenie ma sens czasownik jest dokonany)
	nie dokonany [INFORMUJĄ O WYKONANIU CZYNNOŚCI ALE NIE INFORMUJĄ CZY DANA CZYNNOŚĆ ZOSTAŁA WYKONANA LUB CZY ZAKOŃCZY SIĘ W PRZYSZŁOŚCI]
		- myje
		- obiera
		- kroi
		- bedzie gotowała
		- będzie jadła
	- przeczytał, wyczytał, odczytał, czytał
	
przez tryby [ROZPOZNAJE STOSUNEK MÓWIĄCEGO DO JEGO WYPOWIEDZI. DZIĘKI TRYBOWI WIEMY CO OSOBA WYPOWIADAJĄCA CHCE SWOJĄ WYPOWIEDZIA OSIĄGNĄĆ]
	oznajmujący, orzekający [ZWYKŁE INFORMOWANIE O CZYMŚ, STOSUEK JEST NEUTRANY]
		- Lubię czytać
		- siedzi na krześle
		- jest ubrana wygodnie
	rozkazujacy [SŁUŻY DO WYDAWANIA POLECEŃ LUB ROZKAZÓW BĄDŹ DO WYRAŻANIA ŻYCZENIA LUB PROŚBY]
		- posprzątaj ten bałagan
		- wyprowadź psa
		- usiądź proszę
	przypuszczający [UZYWANY WTEDY GDY WYPOWIADAJĄCY CHCE WYRAŹIĆ WĄTPLIWOŚĆ, PRZYPUSZCZENIE LUB NIEZDECYDOWANIE]
		- zjadłabym dziś pierogi
		- mógłbyś mi w tym pomóc
		- gdybyś mnie wysłuchał
			(zawsze gdy pojawia sie końcówka -byś -bym- by, wskazuje na trzyb przypuszczajacy)
	- przacuje, pracuj, pracowałby

przykłady:
				L. pojedyńcza			L. mnoga
	I. os.		(ja)Otwieram			(my)Otwieramy
	II. os.		(ty)otwierasz			(wy)Otwieracie
	III. os.	(on/ona/ono)Otwiera		(oni/one)Otwierają

przez rodzaje
	męski (on) - zatkał się, udrożnił
	żeński (ona) - przytuliła, będzie badała
	nijaki (ono) bawiło się, grzechotało
	męsko osobowy (oni) będą tańczyli, napisali
	niemęsko osobowy (one) szumiały, ćwiczyły
	- leżał, leżała, leżało, leżeli, leżały
MOŻNA JE ROZPOZNAĆ TYLKO W CZASIE PRZESŁYM I PRZYSZŁYM ZŁOŻONYM ORAZ W RYBIE PRZYPUSZCZAJACYM


"""