# Currencies information: contains the most common 92 currencies.
CURRENCY_INFO = {
    "USD": {"country": "United States", "flag": "us", "currency": "US Dollar", "symbol": "$"},
    "EUR": {"country": "European Union", "flag": "eu", "currency": "Euro", "symbol": "€"},
    "GBP": {"country": "United Kingdom", "flag": "gb", "currency": "British Pound", "symbol": "£"},
    "JPY": {"country": "Japan", "flag": "jp", "currency": "Japanese Yen", "symbol": "¥"},
    "CNY": {"country": "China", "flag": "cn", "currency": "Chinese Yuan", "symbol": "¥"},
    "CAD": {"country": "Canada", "flag": "ca", "currency": "Canadian Dollar", "symbol": "$"},
    "AUD": {"country": "Australia", "flag": "au", "currency": "Australian Dollar", "symbol": "$"},
    "CHF": {"country": "Switzerland", "flag": "ch", "currency": "Swiss Franc", "symbol": "CHF"},
    "EGP": {"country": "Egypt", "flag": "eg", "currency": "Egyptian Pound", "symbol": "£"},
    "SAR": {"country": "Saudi Arabia", "flag": "sa", "currency": "Saudi Riyal", "symbol": "﷼"},
    "AED": {"country": "United Arab Emirates", "flag": "ae", "currency": "UAE Dirham", "symbol": "د.إ"},
    "INR": {"country": "India", "flag": "in", "currency": "Indian Rupee", "symbol": "₹"},
    "RUB": {"country": "Russia", "flag": "ru", "currency": "Russian Ruble", "symbol": "₽"},
    "BRL": {"country": "Brazil", "flag": "br", "currency": "Brazilian Real", "symbol": "R$"},
    "ZAR": {"country": "South Africa", "flag": "za", "currency": "South African Rand", "symbol": "R"},
    "KRW": {"country": "South Korea", "flag": "kr", "currency": "South Korean Won", "symbol": "₩"},
    "SEK": {"country": "Sweden", "flag": "se", "currency": "Swedish Krona", "symbol": "kr"},
    "NOK": {"country": "Norway", "flag": "no", "currency": "Norwegian Krone", "symbol": "kr"},
    "TRY": {"country": "Turkey", "flag": "tr", "currency": "Turkish Lira", "symbol": "₺"},
    "MXN": {"country": "Mexico", "flag": "mx", "currency": "Mexican Peso", "symbol": "$"},
    "SGD": {"country": "Singapore", "flag": "sg", "currency": "Singapore Dollar", "symbol": "$"},
    "NZD": {"country": "New Zealand", "flag": "nz", "currency": "New Zealand Dollar", "symbol": "$"},
    "HKD": {"country": "Hong Kong", "flag": "hk", "currency": "Hong Kong Dollar", "symbol": "$"},
    "PLN": {"country": "Poland", "flag": "pl", "currency": "Polish Złoty", "symbol": "zł"},
    "THB": {"country": "Thailand", "flag": "th", "currency": "Thai Baht", "symbol": "฿"},
    "DKK": {"country": "Denmark", "flag": "dk", "currency": "Danish Krone", "symbol": "kr"},
    "PKR": {"country": "Pakistan", "flag": "pk", "currency": "Pakistani Rupee", "symbol": "₨"},
    "BDT": {"country": "Bangladesh", "flag": "bd", "currency": "Bangladeshi Taka", "symbol": "৳"},
    "NGN": {"country": "Nigeria", "flag": "ng", "currency": "Nigerian Naira", "symbol": "₦"},
    "TWD": {"country": "Taiwan", "flag": "tw", "currency": "New Taiwan Dollar", "symbol": "NT$"},
    "ILS": {"country": "Palestine", "flag": "ps", "currency": "Palestinian Shekel", "symbol": "₪"},
    "MYR": {"country": "Malaysia", "flag": "my", "currency": "Malaysian Ringgit", "symbol": "RM"},
    "PHP": {"country": "Philippines", "flag": "ph", "currency": "Philippine Peso", "symbol": "₱"},
    "CZK": {"country": "Czech Republic", "flag": "cz", "currency": "Czech Koruna", "symbol": "Kč"},
    "HUF": {"country": "Hungary", "flag": "hu", "currency": "Hungarian Forint", "symbol": "Ft"},
    "IDR": {"country": "Indonesia", "flag": "id", "currency": "Indonesian Rupiah", "symbol": "Rp"},
    "CLP": {"country": "Chile", "flag": "cl", "currency": "Chilean Peso", "symbol": "$"},
    "COP": {"country": "Colombia", "flag": "co", "currency": "Colombian Peso", "symbol": "$"},
    "ARS": {"country": "Argentina", "flag": "ar", "currency": "Argentine Peso", "symbol": "$"},
    "VND": {"country": "Vietnam", "flag": "vn", "currency": "Vietnamese Dong", "symbol": "₫"},
    "KWD": {"country": "Kuwait", "flag": "kw", "currency": "Kuwaiti Dinar", "symbol": "د.ك"},
    "QAR": {"country": "Qatar", "flag": "qa", "currency": "Qatari Riyal", "symbol": "ر.ق"},
    "OMR": {"country": "Oman", "flag": "om", "currency": "Omani Rial", "symbol": "ر.ع."},
    "BHD": {"country": "Bahrain", "flag": "bh", "currency": "Bahraini Dinar", "symbol": "ب.د"},
    "UAH": {"country": "Ukraine", "flag": "ua", "currency": "Ukrainian Hryvnia", "symbol": "₴"},
    "LKR": {"country": "Sri Lanka", "flag": "lk", "currency": "Sri Lankan Rupee", "symbol": "Rs"},
    "MAD": {"country": "Morocco", "flag": "ma", "currency": "Moroccan Dirham", "symbol": "د.م."},
    "TZS": {"country": "Tanzania", "flag": "tz", "currency": "Tanzanian Shilling", "symbol": "TSh"},
    "KES": {"country": "Kenya", "flag": "ke", "currency": "Kenyan Shilling", "symbol": "KSh"},
    "GHS": {"country": "Ghana", "flag": "gh", "currency": "Ghanaian Cedi", "symbol": "GH₵"},
    "DZD": {"country": "Algeria", "flag": "dz", "currency": "Algerian Dinar", "symbol": "د.ج"},
    "JOD": {"country": "Jordan", "flag": "jo", "currency": "Jordanian Dinar", "symbol": "د.ا"},
    "LBP": {"country": "Lebanon", "flag": "lb", "currency": "Lebanese Pound", "symbol": "ل.ل"},
    "SDG": {"country": "Sudan", "flag": "sd", "currency": "Sudanese Pound", "symbol": "ج.س"},
    "ETB": {"country": "Ethiopia", "flag": "et", "currency": "Ethiopian Birr", "symbol": "Br"},
    "MMK": {"country": "Myanmar", "flag": "mm", "currency": "Myanmar Kyat", "symbol": "K"},
    "KHR": {"country": "Cambodia", "flag": "kh", "currency": "Cambodian Riel", "symbol": "៛"},
    "LAK": {"country": "Laos", "flag": "la", "currency": "Lao Kip", "symbol": "₭"},
    "AFN": {"country": "Afghanistan", "flag": "af", "currency": "Afghan Afghani", "symbol": "؋"},
    "ALL": {"country": "Albania", "flag": "al", "currency": "Albanian Lek", "symbol": "L"},
    "AMD": {"country": "Armenia", "flag": "am", "currency": "Armenian Dram", "symbol": "֏"},
    "AZN": {"country": "Azerbaijan", "flag": "az", "currency": "Azerbaijani Manat", "symbol": "₼"},
    "BAM": {"country": "Bosnia and Herzegovina", "flag": "ba", "currency": "Convertible Mark", "symbol": "KM"},
    "BIF": {"country": "Burundi", "flag": "bi", "currency": "Burundian Franc", "symbol": "FBu"},
    "BWP": {"country": "Botswana", "flag": "bw", "currency": "Botswana Pula", "symbol": "P"},
    "CDF": {"country": "Democratic Republic of the Congo", "flag": "cd", "currency": "Congolese Franc", "symbol": "FC"},
    "CVE": {"country": "Cape Verde", "flag": "cv", "currency": "Cape Verdean Escudo", "symbol": "$"},
    "DJF": {"country": "Djibouti", "flag": "dj", "currency": "Djiboutian Franc", "symbol": "Fdj"},
    "DOP": {"country": "Dominican Republic", "flag": "do", "currency": "Dominican Peso", "symbol": "RD$"},
    "ERN": {"country": "Eritrea", "flag": "er", "currency": "Eritrean Nakfa", "symbol": "Nfk"},
    "FJD": {"country": "Fiji", "flag": "fj", "currency": "Fijian Dollar", "symbol": "$"},
    "GEL": {"country": "Georgia", "flag": "ge", "currency": "Georgian Lari", "symbol": "₾"},
    "GTQ": {"country": "Guatemala", "flag": "gt", "currency": "Guatemalan Quetzal", "symbol": "Q"},
    "HRK": {"country": "Croatia", "flag": "hr", "currency": "Croatian Kuna", "symbol": "kn"},
    "ISK": {"country": "Iceland", "flag": "is", "currency": "Icelandic Króna", "symbol": "kr"},
    "JMD": {"country": "Jamaica", "flag": "jm", "currency": "Jamaican Dollar", "symbol": "J$"},
    "KGS": {"country": "Kyrgyzstan", "flag": "kg", "currency": "Kyrgyzstani Som", "symbol": "лв"},
    "KZT": {"country": "Kazakhstan", "flag": "kz", "currency": "Kazakhstani Tenge", "symbol": "₸"},
    "LSL": {"country": "Lesotho", "flag": "ls", "currency": "Lesotho Loti", "symbol": "L"},
    "MGA": {"country": "Madagascar", "flag": "mg", "currency": "Malagasy Ariary", "symbol": "Ar"},
    "MNT": {"country": "Mongolia", "flag": "mn", "currency": "Mongolian Tögrög", "symbol": "₮"},
    "MOP": {"country": "Macau", "flag": "mo", "currency": "Macanese Pataca", "symbol": "MOP$"},
    "MUR": {"country": "Mauritius", "flag": "mu", "currency": "Mauritian Rupee", "symbol": "₨"},
    "NAD": {"country": "Namibia", "flag": "na", "currency": "Namibian Dollar", "symbol": "$"},
    "NPR": {"country": "Nepal", "flag": "np", "currency": "Nepalese Rupee", "symbol": "₨"},
    "PEN": {"country": "Peru", "flag": "pe", "currency": "Peruvian Sol", "symbol": "S/."},
    "RON": {"country": "Romania", "flag": "ro", "currency": "Romanian Leu", "symbol": "lei"},
    "SRD": {"country": "Suriname", "flag": "sr", "currency": "Surinamese Dollar", "symbol": "$"},
    "ZWL": {"country": "Zimbabwe", "flag": "zw", "currency": "Zimbabwean Dollar", "symbol": "$"},
    "LYD": {"country": "Libya", "flag": "ly", "currency": "Libyan Dinar", "symbol": "ل.د"},
    "BZD": {"country": "Belize", "flag": "bz", "currency": "Belize Dollar", "symbol": "BZ$"},
    "PGK": {"country": "Papua New Guinea", "flag": "pg", "currency": "Papua New Guinean Kina", "symbol": "K"}
}

# Most traded currency pairs worldwide.
MOST_TRADED_PAIRS = [
    ("USD", "EUR"),
    ("USD", "JPY"),
    ("EUR", "GBP"),
    ("USD", "GBP")
]

# 20 different facts about currencies
CURRENCY_FACTS = [
    {
        "topic": "The Origin of the Dollar Sign ($)",
        "text": "The dollar sign ($) originated from Spanish peso notation. It evolved from writing “PS,” where the “S” eventually overlapped the “P.” It became common in the U.S. by the mid‑1800s. Its symbolism later influenced digital currencies like Bitcoin to borrow its credibility."
    },
    {
        "topic": "Global Currency Dominance (2025)",
        "text": "As of Q1 2025, the U.S. dollar made up ~57.7% of global reserves, while the euro rose to 20.1%—its highest since 2022—and the Swiss franc quadrupled to ~0.8%."
    },
    {
        "topic": "The Era of Trillion-Dollar Bills",
        "text": "Hyperinflation has led to trillion‑unit currencies: Germany in 1923 issued 100‑trillion mark notes; Hungary in 1946 reached the largest denomination ever; Zimbabwe’s 2008 note topped 100 trillion."
    },
    {
        "topic": "Only 8% of Money Is Physical",
        "text": "Only about 8% of the world’s money exists in physical form, with the rest entirely digital."
    },
    {
        "topic": " The Oldest Currency Still in Use",
        "text": "The British pound sterling is the oldest currency still in use, dating back to Anglo‑Saxon England around 775 AD."
    },
    {
        "topic": "Knife-Shaped Coins in Ancient China",
        "text": "Ancient Chinese “knife money”: knife‑shaped bronze coins circulated between 600–200 BC in the Zhou dynasty—some auctioning today for over $140,000."
    },
    {
        "topic": "When Tea and Feathers Were Money",
        "text": "Objects from shells to tea bricks were once used as currency: pre‑Lydian barter systems used livestock or shells; Guatemalan quetzal tail‑feathers were once currency; compressed tea bricks served in Asia."
    },
    {
        "topic": "Banknote Bloopers Worth Thousands",
        "text": "Some banknotes hold design quirks: a British 20‑p coin minted without a date (2008) commands collectible premium; U.S. $5 bills with misprints can be worth up to $400,000.",
    },
    {
        "topic": "The Face of Currency: Queen Elizabeth II",
        "text": "Queen Elizabeth II appeared on more currencies than anyone else—over 35 countries issued coins or notes with her portrait."
    },
    {
        "topic": "Curious Cases of Local Currencies",
        "text": "Unique local currencies and peg systems: Liechtenstein uses Swiss francs exclusively but issues commemorative Swiss coins; Biafra and Alderney issued their own short-lived currencies that now appear in collector circles."
    },
    {
        "topic": "Why We Trust Money",
        "text": "Currency is a symbol of trust, not intrinsic value: modern fiat money is backed by governments and central banks, not by gold or other assets"
    },
    {
        "topic": "The Space Currency That Never Took Off",
        "text": "The Malaysian “QUID” was a proposed space‑focused currency, imagined as inert, safe money for interplanetary travel—part of futuristic currency experiments"
    },
    {
        "topic": "Secrets in the Euro Design",
        "text": "Euro design carries hidden meaning: the “€” is based on the Greek epsilon, and the two horizontal lines symbolize stability and unity within Europe"
    },
    {
        "topic": "Non‑Decimal Currencies Still Exist",
        "text": "Only two currencies today remain non‑decimal: Mauritania’s ouguiya and Madagascar’s ariary, each subdivided into 5 khoums or iraimbilanja respectively—a rarity in modern finance."
    },
    {
        "topic": "China’s Flying Money",
        "text": "The first paper money—called “Flying Money”—originated in China around the 7th–11th centuries, making it easier and lighter to carry than coins."
    },
    {
        "topic": "A Currency That Outlived Empires",
        "text": "The British pound sterling is the oldest currency still in continuous use, dating back to Anglo‑Saxon England in the 8th century."
    },
    {
        "topic": "180 Currencies, One Financial World",
        "text": "There are roughly 180 official currencies worldwide, each backed and regulated by a country or region."
    },
    {
        "topic": "The World’s Most Valuable Currency",
        "text": "The Kuwaiti dinar is the world’s most valuable currency, currently worth around €2.93 per unit, reflecting Kuwait’s economic strength."
    },
    {
        "topic": "Most U.S. Dollars Are Used Abroad",
        "text": "One‑half to two‑thirds of U.S. dollars in circulation are held outside the United States—showing the dollar’s global reach."
    },
    {
        "topic": "Unofficial Euro Users: Kosovo and Mayotte",
        "text": "Kosovo and Mayotte both use the Euro, but neither is part of the Eurozone officially — Kosovo adopted it unilaterally, and Mayotte uses it as a French overseas department."
    }
]


### End if info.py ###
