# SAVC
(A) Simple Audio-Video Combiner, jeb
Vienkāršs Audio-Video Savienotājs

# Projekta apraksts:

Bieži vien cilvēkiem, kuri nodarbojas ar video-audio produkciju, ir nepieciešams atvieglots un parasts veids kā apvienot šīs abas lietas lai varētu izveidot, piemēram, vienkāršu videoklipu ar bildi un kādu dziesmu vai skaņas efektu. Šis rīks ir izstrādāts tā, lai viss šis process notiktu ar tik dažām darbībām.

## Rīka izmantošana

Lietotājs iemet audio/bilžu materiālus norādītajā materiālu mapē (pēc noklusējuma mapē 'dump'), atver programmu, uzraksta vārdu 'create' un programma vienkārši apvieno iemestos materiālus vienā videoklipā. Lietotājam arī ir pieejama iespēja rediģēt pāris parametrus, piemēram, bilžu izšķirtspēju vai arī nomainīt materiālu mapes vai izvadītā videoklipa nosaukumu uz ko citu. To var izdarīt programmā ievadot vārdu 'edit'. Pēc šīs komandas izpildes, tiek izvadīti parametri, kurus var rediģēt. Lai rediģētu parametru ir jāievada tā vārds un jānospiež ENTER. Tālāk ir jāievada jauno parametra vērtību un atkal jānospiež ENTER. Visu pabeidzot, jāievada komandu "exit" vai "quit" lai atgrieztos galvenajā panelī.

### "Stretch" režīms

"Stretch" režīms ņem visas bildes no mapes un videoklipā tās saliek vienādā laikā starp audio-failiem.
Ja "Stretch" lietotāja preferencēs ir "false", tad bildes mainās tikai tad, kad sākas nākamais audio-fails.

## Praktiskais pielietojums

Lietotājs šo rīku var izmantot, lai apvienotu audio (dziesmu, vai vairākas dziesmas) un bildes vienā videoklipā jebkāda iemesla pēc.
Praktiski šo rīku var pielietot cilvēki, kuriem ir nepieciešams ļoti ātri un vienkārši izlikt mūzikas albumu (vai vienu dziesmu) video-failā interneta pakalpojumos, piemēram, YouTube vai vienkārši atsūtīt bildi ar dziesmu (vai skaņas efektu) videoklipā draugiem caur Discord.

## Projekta Mērķis:
Projekta mērķis ir atvieglot un automatizēt pavisam vienkāršu videoklipu veidošanu audio-video materiālu producētājiem, bez nepieciešamības vērt vaļā video redaktora rīku.

# Izmantotās Python bibliotēkas

Šis projekts izmanto PIL un MoviePy.

PIL tiek pielietots, lai ļoti vienkārši varētu rediģēt bildes un to izšķirtspēju, nomainīt bit-depth definīcijas.

MoviePy tiek pielietots, lai izveidotu video failus un apvienotu gan audio, gan video daļas.

## demonstratīvs videoklips

[Video](https://youtu.be/92nSoJlj7AU?si=CpBAZQ6UZ1l6C0Uq)
