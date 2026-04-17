-###-  BACK-END
   • per le funzionalità di prenotazione e pagamento sul sito serve creare una infrastruttura back-end che funzioni tramite varie API,
        per cui ho creato una repository privata apposita dove poi ci svilupperò il codice:
           - PAGAMENTI: Stripe API per il gateway dei pagamenti (offre Apple Pay e quant'altro).
           - CALENDARIO: Firebase + iCal per l'aggiornamento continuo del calendario delle disponibilità (le API delle OTA sono inaccessibili).
           - BLOG

-###- BLOG
   • alcuni siti la chiamano invece sezione "notebook"
        - richiede importanti sviluppi del back-end

-###- LINGUE
   • NON si crea un html per ogni lingua, bensì si opta per uno di questi tre approcci;
      - json + js : si crea un file json che contiene tutte le stringhe del sito ed implementi la funzione changeLanguage, 
           mentre nel file html invece di scrivere i testi ti riferisci ad un determinato testo usando le data-key.
      - url + sotto-directories : approccio migliore per la SEO.
      - librerie o API : librerie come i18Next oppure widget come Google Translate API o Weglot 
   • La Soluzione Migliore:
      (1) aggiungere l'attributo data-i18n ad ogni testo o riga nell'html; (2) creare un oggetto js con tutte le traduzioni;
      (3) implementare una funzione SetLanguage nel js; (4) inserire nell'html il menù di selezione della lingua.
      - italiano, inglese, spagnolo, russo, tedesco, cinese ---> tramite IA, cioè niente google translate.

-###- PROMPT ESAGERATO
"Ora come ora dopo l'animazione introduttiva ci sono gli "elementi" che appaiono tutti insieme, 
   invece vorrei che apparissero in maniera incrementale ma senza troppa latenza; ->
   una specie di microintroduzione di tutto il sito successiva all'animazione iniziale che faccia apparire il tutto un pò più smooth non so se mi spiego. 
Inoltre, vorrei che scrollando apparissero le cose e non che scrolli e vedi che stanno già tutte lì non so se mi spiego; 
   questo però è una "apparizione dinamica" diversa da quella iniziale che ho poc'anzi detto perchè questa è collegata allo scroll sul sito,
   mentre la prima che intendevo sarebbe correlata all'accesso al sito ed al momento immediatamente successivo alla conclusione dell'animazione. 
La sezione blog però da quanto ho capito complica la situazione perchè ora come ora non lo so, 
   cioè dovrebbe esserci nella sezione blog una pagina iniziale con tutti quadratini dei post/articoli e tu clicchi sul singolo articolo 
   e te lo fa leggere ma significa che periodicamente devo aggiungere un articolo quindi non so come funziona il tutto. 
Il tutto si complica anche considerando che per ora il sito non offre nulla per chi non parla italiano ma molti siti offrono la possibilità di tradurre 
   in una determinata lingua semplicemente selezionandola tra quelle in una lista a comparsa che compare cliccando su un apposito tasto che 
   di solito appare come semplice "italiano" se attualmente la lingua selezionata è l'italiano, non so se mi spiego ma è una cosa abbastanza standard. 
