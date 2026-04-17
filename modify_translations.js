const fs = require('fs');

const path = 'translations.js';
let content = fs.readFileSync(path, 'utf8');

// The file is typical front-end JS: `window.translations = { ... };`
// I can do some regex to insert keys right before the end of each language block.

const newKeys = {
    "it": {
        "blog_read_more": "Leggi di più →",
        "blog_toraldo_desc": "Nel cuore della Costa degli Dei, tra le scogliere di Tropea e le spiagge cristalline di Santa Domenica di Ricadi, la figura dell’imperatore Federico II si intreccia con la nobile famiglia Toraldo...",
        "faq_q1": "A che distanza si trovano le spiagge?",
        "faq_a1": "Ci troviamo sulla costa, circondati da tutte le spiagge principali della zona.",
        "faq_q2": "Il WiFi è disponibile?",
        "faq_a2": "Sì, è gratuito e copre per intero le strutture.",
        "faq_q3": "Viene fornita la biancheria?",
        "faq_a3": "Certamente, è disponibile su richiesta per garantirvi il massimo comfort.",
        "faq_q4": "Gli animali domestici sono ammessi?",
        "faq_a4": "Solamente quelli di piccola taglia.",
        "faq_q5": "È consentito fumare all'interno?",
        "faq_a5": "No, è severamente vietato e punito con una multa.",
        "reviews_title": "Cosa dicono i nostri ospiti",
        "service_bbq": "Barbecue",
        "service_excursion": "Escursioni"
    },
    "en": {
        "blog_read_more": "Read more →",
        "blog_toraldo_desc": "In the heart of the Coast of the Gods, between the cliffs of Tropea and the crystal clear beaches of Santa Domenica di Ricadi, the figure of Emperor Frederick II intertwines with the noble Toraldo family...",
        "faq_q1": "How far are the beaches?",
        "faq_a1": "We are located right on the coast, surrounded by all the main beaches of the area.",
        "faq_q2": "Is WiFi available?",
        "faq_a2": "Yes, it is free and covers the entire property.",
        "faq_q3": "Is bed linen provided?",
        "faq_a3": "Certainly, it is available upon request to ensure maximum comfort.",
        "faq_q4": "Are pets allowed?",
        "faq_a4": "Only small pets are welcome.",
        "faq_q5": "Is smoking allowed inside?",
        "faq_a5": "No, smoking is strictly forbidden indoors and is subject to a fine.",
        "reviews_title": "What our guests say",
        "service_bbq": "BBQ",
        "service_excursion": "Excursions"
    },
    "es": {
        "blog_read_more": "Leer más →",
        "blog_toraldo_desc": "En el corazón de la Costa de los Dioses, entre los acantilados de Tropea y las cristalinas playas de Santa Domenica de Ricadi, la figura del emperador Federico II se entrelaza con la noble familia Toraldo...",
        "faq_q1": "¿A qué distancia están las playas?",
        "faq_a1": "Estamos ubicados en la costa, rodeados de las principales playas de la zona.",
        "faq_q2": "¿Hay WiFi disponible?",
        "faq_a2": "Sí, es gratuito y cubre toda la propiedad.",
        "faq_q3": "¿Se proporciona ropa de cama?",
        "faq_a3": "Por supuesto, está disponible bajo petición para garantizar su máximo confort.",
        "faq_q4": "¿Se admiten mascotas?",
        "faq_a4": "Solo se admiten mascotas pequeñas.",
        "faq_q5": "¿Se permite fumar en el interior?",
        "faq_a5": "No, está estrictamente prohibido fumar en el interior y conlleva una multa.",
        "reviews_title": "Lo que dicen nuestros huéspedes",
        "service_bbq": "Barbacoa",
        "service_excursion": "Excursiones"
    },
    "ru": {
        "blog_read_more": "Читать далее →",
        "blog_toraldo_desc": "В самом сердце Побережья Богов, между скалами Тропеи и кристально чистыми пляжами Санта-Доменика-ди-Рикади, фигура императора Фридриха II переплетается со знатным родом Торальдо...",
        "faq_q1": "Как далеко находятся пляжи?",
        "faq_a1": "Мы находимся на побережье, в окружении всех главных пляжей района.",
        "faq_q2": "Есть ли Wi-Fi?",
        "faq_a2": "Да, бесплатный Wi-Fi покрывает всю территорию.",
        "faq_q3": "Предоставляется ли постельное белье?",
        "faq_a3": "Конечно, оно предоставляется по запросу для обеспечения максимального комфорта.",
        "faq_q4": "Разрешено ли проживание с домашними животными?",
        "faq_a4": "Допускаются только домашние животные небольшого размера.",
        "faq_q5": "Разрешено ли курить в помещении?",
        "faq_a5": "Нет, курение в помещении строго запрещено и наказывается штрафом.",
        "reviews_title": "Что говорят наши гости",
        "service_bbq": "Барбекю",
        "service_excursion": "Экскурсии"
    },
    "de": {
        "blog_read_more": "Weiterlesen →",
        "blog_toraldo_desc": "Im Herzen der Küste der Götter, zwischen den Klippen von Tropea und den kristallklaren Stränden von Santa Domenica di Ricadi, verwebt sich die Figur von Kaiser Friedrich II. mit der Adelsfamilie Toraldo...",
        "faq_q1": "Wie weit sind die Strände entfernt?",
        "faq_a1": "Wir befinden uns direkt an der Küste, umgeben von allen wichtigen Stränden der Umgebung.",
        "faq_q2": "Ist WLAN verfügbar?",
        "faq_a2": "Ja, es ist kostenlos und deckt die gesamte Unterkunft ab.",
        "faq_q3": "Wird Bettwäsche gestellt?",
        "faq_a3": "Selbstverständlich, sie ist auf Anfrage erhältlich, um Ihren maximalen Komfort zu gewährleisten.",
        "faq_q4": "Sind Haustiere erlaubt?",
        "faq_a4": "Nur kleine Haustiere sind willkommen.",
        "faq_q5": "Ist Rauchen im Haus erlaubt?",
        "faq_a5": "Nein, Rauchen ist in den Innenräumen strengstens verboten und wird mit einem Bußgeld geahndet.",
        "reviews_title": "Das sagen unsere Gäste",
        "service_bbq": "Grill",
        "service_excursion": "Ausflüge"
    },
    "zh": {
        "blog_read_more": "阅读更多 →",
        "blog_toraldo_desc": "在诸神海岸的中心，Tropea的悬崖和Santa Domenica di Ricadi清澈的海滩之间，皇帝腓特烈二世的形象与高贵的Toraldo家族交织在一起...",
        "faq_q1": "离海滩有多远？",
        "faq_a1": "我们位于海岸边，周围环绕着该地区所有主要的海滩。",
        "faq_q2": "有WiFi吗？",
        "faq_a2": "有的，免费WiFi覆盖整个酒店。",
        "faq_q3": "提供床单吗？",
        "faq_a3": "当然，我们可应要求提供，以确保您获得最大的舒适度。",
        "faq_q4": "允许携带宠物吗？",
        "faq_a4": "仅欢迎小型宠物。",
        "faq_q5": "室内允许吸烟吗？",
        "faq_a5": "不允许，室内严禁吸烟，违者将被罚款。",
        "reviews_title": "客人的评价",
        "service_bbq": "烧烤",
        "service_excursion": "短途旅行"
    }
}

for (const [lang, keys]] of Object.entries(newKeys)) {
    let toInsert = '';
    for (const [k, v] of Object.entries(keys)) {
        toInsert += `        "${k}": "${v.replace(/"/g, '\\"')}",\n`;
    }
    
    // Find the end of the language block
    // It looks like:
    //    },
    //    "en": {
    // So we search for the end of the lang object.
    
    // Regex to match the end of `lang: { ... }` block
    const regexStr = `("${lang}"|${lang})\\s*:\\s*\\{([\\s\\S]*?)(^\\s*\\})?`;
    const regex = new RegExp(`("${lang}"|${lang})\\s*:\\s*\\{([^\\}]*?)\\n(\\s*)\\}`, 'gm');
    
    content = content.replace(regex, (match, p1, p2, p3) => {
        // match contains the whole block
        // wait, [^\}]* doesn't work if there are nested braces
        return match; 
    });
}
