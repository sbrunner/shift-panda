import os

import pytest

from shifter_pandas.wikidata_ import WikidataDatasource

BP_DATA = [
    ("Canada", "Canada"),
    ("Mexico", "Mexico"),
    ("United States of America", "US"),
    ("North America", "Total North America"),
    ("Argentina", "Argentina"),
    ("Brazil", "Brazil"),
    ("Chile", "Chile"),
    ("Colombia", "Colombia"),
    ("Ecuador", "Ecuador"),
    ("Peru", "Peru"),
    ("Trinidad and Tobago", "Trinidad & Tobago"),
    ("Venezuela", "Venezuela"),
    ("Central America", "Central America"),
    (None, "Other Caribbean"),
    (None, "Other South America"),
    (None, "Total S. & Cent. America"),
    ("Austria", "Austria"),
    ("Belgium", "Belgium"),
    ("Bulgaria", "Bulgaria"),
    ("Croatia", "Croatia"),
    ("Cyprus", "Cyprus"),
    ("Czech Republic", "Czech Republic"),
    ("Denmark", "Denmark"),
    ("Estonia", "Estonia"),
    ("Finland", "Finland"),
    ("France", "France"),
    ("Germany", "Germany"),
    ("Greece", "Greece"),
    ("Hungary", "Hungary"),
    ("Iceland", "Iceland"),
    ("Republic of Ireland", "Ireland"),
    ("Italy", "Italy"),
    ("Latvia", "Latvia"),
    ("Lithuania", "Lithuania"),
    ("Luxembourg", "Luxembourg"),
    ("Netherlands", "Netherlands"),
    ("North Macedonia", "North Macedonia"),
    ("Norway", "Norway"),
    ("Poland", "Poland"),
    ("Portugal", "Portugal"),
    ("Romania", "Romania"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Spain", "Spain"),
    ("Sweden", "Sweden"),
    ("Switzerland", "Switzerland"),
    ("Turkey", "Turkey"),
    ("Ukraine", "Ukraine"),
    ("United Kingdom", "United Kingdom"),
    (None, "Other Europe"),
    ("Europe", "Total Europe"),
    ("Azerbaijan", "Azerbaijan"),
    ("Belarus", "Belarus"),
    ("Kazakhstan", "Kazakhstan"),
    ("Russia", "Russian Federation"),
    ("Turkmenistan", "Turkmenistan"),
    ("Uzbekistan", "Uzbekistan"),
    (None, "Other CIS"),
    (None, "Total CIS"),
    ("Iran", "Iran"),
    ("Iraq", "Iraq"),
    ("Israel", "Israel"),
    ("Kuwait", "Kuwait"),
    ("Oman", "Oman"),
    ("Qatar", "Qatar"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("United Arab Emirates", "United Arab Emirates"),
    (None, "Other Middle East"),
    ("Middle East", "Total Middle East"),
    ("Algeria", "Algeria"),
    ("Egypt", "Egypt"),
    ("Morocco", "Morocco"),
    ("South Africa", "South Africa"),
    ("East Africa", "Eastern Africa"),
    ("Middle Africa", "Middle Africa"),
    ("West Africa", "Western Africa"),
    (None, "Other Northern Africa"),
    (None, "Other Southern Africa"),
    ("Africa", "Total Africa"),
    ("Australia", "Australia"),
    ("Bangladesh", "Bangladesh"),
    ("People's Republic of China", "China"),
    ("Hong Kong", "China Hong Kong SAR"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Japan", "Japan"),
    ("Malaysia", "Malaysia"),
    ("New Zealand", "New Zealand"),
    ("Pakistan", "Pakistan"),
    ("Philippines", "Philippines"),
    ("Singapore", "Singapore"),
    ("South Korea", "South Korea"),
    ("Sri Lanka", "Sri Lanka"),
    ("Taiwan", "Taiwan"),
    ("Thailand", "Thailand"),
    ("Vietnam", "Vietnam"),
    (None, "Other Asia Pacific"),
    ("Asia-Pacific", "Total Asia Pacific"),
    ("World", "Total World"),
    (None, "of which: OECD"),
    (None, "                 Non-OECD"),
    ("European Union", "                 European Union #"),
]

WORLD_IN_DATA_DATA = [
    ("Afghanistan", "AFG", "Asia", "Afghanistan"),
    ("Africa", "OWID_AFR", None, "Africa"),
    ("Albania", "ALB", "Europe", "Albania"),
    ("Algeria", "DZA", "Africa", "Algeria"),
    ("Andorra", "AND", "Europe", "Andorra"),
    ("Angola", "AGO", "Africa", "Angola"),
    ("Anguilla", "AIA", "North America", "Anguilla"),
    ("Antigua and Barbuda", "ATG", "North America", "Antigua and Barbuda"),
    ("Argentina", "ARG", "South America", "Argentina"),
    ("Armenia", "ARM", "Asia", "Armenia"),
    ("Aruba", "ABW", "North America", "Aruba"),
    ("Asia", "OWID_ASI", None, "Asia"),
    ("Australia", "AUS", "Oceania", "Australia"),
    ("Austria", "AUT", "Europe", "Austria"),
    ("Azerbaijan", "AZE", "Asia", "Azerbaijan"),
    ("The Bahamas", "BHS", "North America", "Bahamas"),
    ("Bahrain", "BHR", "Asia", "Bahrain"),
    ("Bangladesh", "BGD", "Asia", "Bangladesh"),
    ("Barbados", "BRB", "North America", "Barbados"),
    ("Belarus", "BLR", "Europe", "Belarus"),
    ("Belgium", "BEL", "Europe", "Belgium"),
    ("Belize", "BLZ", "North America", "Belize"),
    ("Benin", "BEN", "Africa", "Benin"),
    ("Bermuda", "BMU", "North America", "Bermuda"),
    ("Bhutan", "BTN", "Asia", "Bhutan"),
    ("Bolivia", "BOL", "South America", "Bolivia"),
    #    ("Bonaire Sint Eustatius and Saba", "BES", "North America", "Bonaire Sint Eustatius and Saba"),
    ("Bosnia and Herzegovina", "BIH", "Europe", "Bosnia and Herzegovina"),
    ("Botswana", "BWA", "Africa", "Botswana"),
    ("Brazil", "BRA", "South America", "Brazil"),
    ("British Virgin Islands", "VGB", "North America", "British Virgin Islands"),
    ("Brunei", "BRN", "Asia", "Brunei"),
    ("Bulgaria", "BGR", "Europe", "Bulgaria"),
    ("Burkina Faso", "BFA", "Africa", "Burkina Faso"),
    ("Burundi", "BDI", "Africa", "Burundi"),
    ("Cambodia", "KHM", "Asia", "Cambodia"),
    ("Cameroon", "CMR", "Africa", "Cameroon"),
    ("Canada", "CAN", "North America", "Canada"),
    ("Cape Verde", "CPV", "Africa", "Cape Verde"),
    ("Cayman Islands", "CYM", "North America", "Cayman Islands"),
    ("Central African Republic", "CAF", "Africa", "Central African Republic"),
    ("Chad", "TCD", "Africa", "Chad"),
    ("Chile", "CHL", "South America", "Chile"),
    ("People's Republic of China", "CHN", "Asia", "China"),
    ("Colombia", "COL", "South America", "Colombia"),
    ("Comoros", "COM", "Africa", "Comoros"),
    ("Republic of the Congo", "COG", "Africa", "Congo"),
    ("Cook Islands", "COK", "Oceania", "Cook Islands"),
    ("Costa Rica", "CRI", "North America", "Costa Rica"),
    ("Côte d'Ivoire", "CIV", "Africa", "Cote d'Ivoire"),
    ("Croatia", "HRV", "Europe", "Croatia"),
    ("Cuba", "CUB", "North America", "Cuba"),
    ("Curaçao", "CUW", "North America", "Curacao"),
    ("Cyprus", "CYP", "Europe", "Cyprus"),
    ("Czech Republic", "CZE", "Europe", "Czechia"),
    ("Democratic Republic of the Congo", "COD", "Africa", "Democratic Republic of Congo"),
    ("Denmark", "DNK", "Europe", "Denmark"),
    ("Djibouti", "DJI", "Africa", "Djibouti"),
    ("Dominica", "DMA", "North America", "Dominica"),
    ("Dominican Republic", "DOM", "North America", "Dominican Republic"),
    ("Ecuador", "ECU", "South America", "Ecuador"),
    ("Egypt", "EGY", "Africa", "Egypt"),
    ("El Salvador", "SLV", "North America", "El Salvador"),
    ("Equatorial Guinea", "GNQ", "Africa", "Equatorial Guinea"),
    ("Eritrea", "ERI", "Africa", "Eritrea"),
    ("Estonia", "EST", "Europe", "Estonia"),
    ("Eswatini", "SWZ", "Africa", "Eswatini"),
    ("Ethiopia", "ETH", "Africa", "Ethiopia"),
    ("Europe", "OWID_EUR", None, "Europe"),
    ("European Union", "OWID_EUN", None, "European Union"),
    ("Faroe Islands", "FRO", "Europe", "Faeroe Islands"),
    ("Falkland Islands", "FLK", "South America", "Falkland Islands"),
    ("Fiji", "FJI", "Oceania", "Fiji"),
    ("Finland", "FIN", "Europe", "Finland"),
    ("France", "FRA", "Europe", "France"),
    ("French Polynesia", "PYF", "Oceania", "French Polynesia"),
    ("Gabon", "GAB", "Africa", "Gabon"),
    ("The Gambia", "GMB", "Africa", "Gambia"),
    ("Georgia", "GEO", "Asia", "Georgia"),
    ("Germany", "DEU", "Europe", "Germany"),
    ("Ghana", "GHA", "Africa", "Ghana"),
    ("Gibraltar", "GIB", "Europe", "Gibraltar"),
    ("Greece", "GRC", "Europe", "Greece"),
    ("Greenland", "GRL", "North America", "Greenland"),
    ("Grenada", "GRD", "North America", "Grenada"),
    ("Guatemala", "GTM", "North America", "Guatemala"),
    ("Guernsey", "GGY", "Europe", "Guernsey"),
    ("Guinea", "GIN", "Africa", "Guinea"),
    ("Guinea-Bissau", "GNB", "Africa", "Guinea-Bissau"),
    ("Guyana", "GUY", "South America", "Guyana"),
    ("Haiti", "HTI", "North America", "Haiti"),
    (None, "OWID_HIC", None, "High income"),
    ("Honduras", "HND", "North America", "Honduras"),
    ("Hong Kong", "HKG", "Asia", "Hong Kong"),
    ("Hungary", "HUN", "Europe", "Hungary"),
    ("Iceland", "ISL", "Europe", "Iceland"),
    ("India", "IND", "Asia", "India"),
    ("Indonesia", "IDN", "Asia", "Indonesia"),
    (None, "OWID_INT", None, "International"),
    ("Iran", "IRN", "Asia", "Iran"),
    ("Iraq", "IRQ", "Asia", "Iraq"),
    ("Republic of Ireland", "IRL", "Europe", "Ireland"),
    ("Isle of Man", "IMN", "Europe", "Isle of Man"),
    ("Israel", "ISR", "Asia", "Israel"),
    ("Italy", "ITA", "Europe", "Italy"),
    ("Jamaica", "JAM", "North America", "Jamaica"),
    ("Japan", "JPN", "Asia", "Japan"),
    ("Jersey", "JEY", "Europe", "Jersey"),
    ("Jordan", "JOR", "Asia", "Jordan"),
    ("Kazakhstan", "KAZ", "Asia", "Kazakhstan"),
    ("Kenya", "KEN", "Africa", "Kenya"),
    ("Kiribati", "KIR", "Oceania", "Kiribati"),
    ("Kosovo", "OWID_KOS", "Europe", "Kosovo"),
    ("Kuwait", "KWT", "Asia", "Kuwait"),
    ("Kyrgyzstan", "KGZ", "Asia", "Kyrgyzstan"),
    ("Laos", "LAO", "Asia", "Laos"),
    ("Latvia", "LVA", "Europe", "Latvia"),
    ("Lebanon", "LBN", "Asia", "Lebanon"),
    ("Lesotho", "LSO", "Africa", "Lesotho"),
    ("Liberia", "LBR", "Africa", "Liberia"),
    ("Libya", "LBY", "Africa", "Libya"),
    ("Liechtenstein", "LIE", "Europe", "Liechtenstein"),
    ("Lithuania", "LTU", "Europe", "Lithuania"),
    (None, "OWID_LIC", None, "Low income"),
    (None, "OWID_LMC", None, "Lower middle income"),
    ("Luxembourg", "LUX", "Europe", "Luxembourg"),
    ("Macau", "MAC", "Asia", "Macao"),
    ("Madagascar", "MDG", "Africa", "Madagascar"),
    ("Malawi", "MWI", "Africa", "Malawi"),
    ("Malaysia", "MYS", "Asia", "Malaysia"),
    ("Maldives", "MDV", "Asia", "Maldives"),
    ("Mali", "MLI", "Africa", "Mali"),
    ("Malta", "MLT", "Europe", "Malta"),
    ("Marshall Islands", "MHL", "Oceania", "Marshall Islands"),
    ("Mauritania", "MRT", "Africa", "Mauritania"),
    ("Mauritius", "MUS", "Africa", "Mauritius"),
    ("Mexico", "MEX", "North America", "Mexico"),
    ("Federated States of Micronesia", "FSM", "Oceania", "Micronesia (country)"),
    ("Moldova", "MDA", "Europe", "Moldova"),
    ("Monaco", "MCO", "Europe", "Monaco"),
    ("Mongolia", "MNG", "Asia", "Mongolia"),
    ("Montenegro", "MNE", "Europe", "Montenegro"),
    ("Montserrat", "MSR", "North America", "Montserrat"),
    ("Morocco", "MAR", "Africa", "Morocco"),
    ("Mozambique", "MOZ", "Africa", "Mozambique"),
    ("Myanmar", "MMR", "Asia", "Myanmar"),
    ("Namibia", "NAM", "Africa", "Namibia"),
    ("Nauru", "NRU", "Oceania", "Nauru"),
    ("Nepal", "NPL", "Asia", "Nepal"),
    ("Netherlands", "NLD", "Europe", "Netherlands"),
    ("New Caledonia", "NCL", "Oceania", "New Caledonia"),
    ("New Zealand", "NZL", "Oceania", "New Zealand"),
    ("Nicaragua", "NIC", "North America", "Nicaragua"),
    ("Niger", "NER", "Africa", "Niger"),
    ("Nigeria", "NGA", "Africa", "Nigeria"),
    ("Niue", "NIU", "Oceania", "Niue"),
    ("North America", "OWID_NAM", None, "North America"),
    ("North Macedonia", "MKD", "Europe", "North Macedonia"),
    (None, "OWID_CYN", "Asia", "Northern Cyprus"),
    ("Norway", "NOR", "Europe", "Norway"),
    ("Oceania", "OWID_OCE", None, "Oceania"),
    ("Oman", "OMN", "Asia", "Oman"),
    ("Pakistan", "PAK", "Asia", "Pakistan"),
    ("Palau", "PLW", "Oceania", "Palau"),
    ("Palestinian territories", "PSE", "Asia", "Palestine"),
    ("Panama", "PAN", "North America", "Panama"),
    ("Papua New Guinea", "PNG", "Oceania", "Papua New Guinea"),
    ("Paraguay", "PRY", "South America", "Paraguay"),
    ("Peru", "PER", "South America", "Peru"),
    ("Philippines", "PHL", "Asia", "Philippines"),
    ("Pitcairn Islands", "PCN", "Oceania", "Pitcairn"),
    ("Poland", "POL", "Europe", "Poland"),
    ("Portugal", "PRT", "Europe", "Portugal"),
    ("Qatar", "QAT", "Asia", "Qatar"),
    ("Romania", "ROU", "Europe", "Romania"),
    ("Russia", "RUS", "Europe", "Russia"),
    ("Rwanda", "RWA", "Africa", "Rwanda"),
    ("Saint Helena, Ascension and Tristan da Cunha", "SHN", "Africa", "Saint Helena"),
    ("Saint Kitts and Nevis", "KNA", "North America", "Saint Kitts and Nevis"),
    ("Saint Lucia", "LCA", "North America", "Saint Lucia"),
    ("Saint Pierre and Miquelon", "SPM", "North America", "Saint Pierre and Miquelon"),
    ("Saint Vincent and the Grenadines", "VCT", "North America", "Saint Vincent and the Grenadines"),
    ("Samoa", "WSM", "Oceania", "Samoa"),
    ("San Marino", "SMR", "Europe", "San Marino"),
    ("São Tomé and Príncipe", "STP", "Africa", "Sao Tome and Principe"),
    ("Saudi Arabia", "SAU", "Asia", "Saudi Arabia"),
    ("Senegal", "SEN", "Africa", "Senegal"),
    ("Serbia", "SRB", "Europe", "Serbia"),
    ("Seychelles", "SYC", "Africa", "Seychelles"),
    ("Sierra Leone", "SLE", "Africa", "Sierra Leone"),
    ("Singapore", "SGP", "Asia", "Singapore"),
    ("Sint Maarten", "SXM", "North America", "Sint Maarten (Dutch part)"),
    ("Slovakia", "SVK", "Europe", "Slovakia"),
    ("Slovenia", "SVN", "Europe", "Slovenia"),
    ("Solomon Islands", "SLB", "Oceania", "Solomon Islands"),
    ("Somalia", "SOM", "Africa", "Somalia"),
    ("South Africa", "ZAF", "Africa", "South Africa"),
    ("South America", "OWID_SAM", None, "South America"),
    ("South Korea", "KOR", "Asia", "South Korea"),
    ("South Sudan", "SSD", "Africa", "South Sudan"),
    ("Spain", "ESP", "Europe", "Spain"),
    ("Sri Lanka", "LKA", "Asia", "Sri Lanka"),
    ("Sudan", "SDN", "Africa", "Sudan"),
    ("Suriname", "SUR", "South America", "Suriname"),
    ("Sweden", "SWE", "Europe", "Sweden"),
    ("Switzerland", "CHE", "Europe", "Switzerland"),
    ("Syria", "SYR", "Asia", "Syria"),
    ("Taiwan", "TWN", "Asia", "Taiwan"),
    ("Tajikistan", "TJK", "Asia", "Tajikistan"),
    ("Tanzania", "TZA", "Africa", "Tanzania"),
    ("Thailand", "THA", "Asia", "Thailand"),
    ("East Timor", "TLS", "Asia", "Timor"),
    ("Togo", "TGO", "Africa", "Togo"),
    ("Tokelau", "TKL", "Oceania", "Tokelau"),
    ("Tonga", "TON", "Oceania", "Tonga"),
    ("Trinidad and Tobago", "TTO", "North America", "Trinidad and Tobago"),
    ("Tunisia", "TUN", "Africa", "Tunisia"),
    ("Turkey", "TUR", "Asia", "Turkey"),
    ("Turkmenistan", "TKM", "Asia", "Turkmenistan"),
    ("Turks and Caicos Islands", "TCA", "North America", "Turks and Caicos Islands"),
    ("Tuvalu", "TUV", "Oceania", "Tuvalu"),
    ("Uganda", "UGA", "Africa", "Uganda"),
    ("Ukraine", "UKR", "Europe", "Ukraine"),
    ("United Arab Emirates", "ARE", "Asia", "United Arab Emirates"),
    ("United Kingdom", "GBR", "Europe", "United Kingdom"),
    ("United States of America", "USA", "North America", "United States"),
    (None, "OWID_UMC", None, "Upper middle income"),
    ("Uruguay", "URY", "South America", "Uruguay"),
    ("Uzbekistan", "UZB", "Asia", "Uzbekistan"),
    ("Vanuatu", "VUT", "Oceania", "Vanuatu"),
    ("Vatican City", "VAT", "Europe", "Vatican"),
    ("Venezuela", "VEN", "South America", "Venezuela"),
    ("Vietnam", "VNM", "Asia", "Vietnam"),
    ("Wallis and Futuna", "WLF", "Oceania", "Wallis and Futuna"),
    ("World", "OWID_WRL", None, "World"),
    ("Yemen", "YEM", "Asia", "Yemen"),
    ("Zambia", "ZMB", "Africa", "Zambia"),
    ("Zimbabwe", "ZWE", "Africa", "Zimbabwe"),
]

WORLDBANK_DATA = [
    ("Aruba", "Aruba", "ABW"),
    (None, "Africa Eastern and Southern", "AFE"),
    ("Afghanistan", "Afghanistan", "AFG"),
    (None, "Africa Western and Central", "AFW"),
    ("Angola", "Angola", "AGO"),
    ("Albania", "Albania", "ALB"),
    ("Andorra", "Andorra", "AND"),
    ("Arab world", "Arab World", "ARB"),
    ("United Arab Emirates", "United Arab Emirates", "ARE"),
    ("Argentina", "Argentina", "ARG"),
    ("Armenia", "Armenia", "ARM"),
    ("American Samoa", "American Samoa", "ASM"),
    ("Antigua and Barbuda", "Antigua and Barbuda", "ATG"),
    ("Australia", "Australia", "AUS"),
    ("Austria", "Austria", "AUT"),
    ("Azerbaijan", "Azerbaijan", "AZE"),
    ("Burundi", "Burundi", "BDI"),
    ("Belgium", "Belgium", "BEL"),
    ("Benin", "Benin", "BEN"),
    ("Burkina Faso", "Burkina Faso", "BFA"),
    ("Bangladesh", "Bangladesh", "BGD"),
    ("Bulgaria", "Bulgaria", "BGR"),
    ("Bahrain", "Bahrain", "BHR"),
    ("The Bahamas", "Bahamas, The", "BHS"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina", "BIH"),
    ("Belarus", "Belarus", "BLR"),
    ("Belize", "Belize", "BLZ"),
    ("Bermuda", "Bermuda", "BMU"),
    ("Bolivia", "Bolivia", "BOL"),
    ("Brazil", "Brazil", "BRA"),
    ("Barbados", "Barbados", "BRB"),
    ("Brunei", "Brunei Darussalam", "BRN"),
    ("Bhutan", "Bhutan", "BTN"),
    ("Botswana", "Botswana", "BWA"),
    ("Central African Republic", "Central African Republic", "CAF"),
    ("Canada", "Canada", "CAN"),
    (None, "Central Europe and the Baltics", "CEB"),
    ("Switzerland", "Switzerland", "CHE"),
    ("Chile", "Chile", "CHL"),
    ("People's Republic of China", "China", "CHN"),
    ("Côte d'Ivoire", "Cote d'Ivoire", "CIV"),
    ("Cameroon", "Cameroon", "CMR"),
    ("Democratic Republic of the Congo", "Congo, Dem. Rep.", "COD"),
    ("Republic of the Congo", "Congo, Rep.", "COG"),
    ("Colombia", "Colombia", "COL"),
    ("Comoros", "Comoros", "COM"),
    ("Cape Verde", "Cabo Verde", "CPV"),
    ("Costa Rica", "Costa Rica", "CRI"),
    (None, "Caribbean small states", "CSS"),
    ("Cuba", "Cuba", "CUB"),
    ("Curaçao", "Curacao", "CUW"),
    ("Cayman Islands", "Cayman Islands", "CYM"),
    ("Cyprus", "Cyprus", "CYP"),
    ("Czech Republic", "Czech Republic", "CZE"),
    ("Germany", "Germany", "DEU"),
    ("Djibouti", "Djibouti", "DJI"),
    ("Dominica", "Dominica", "DMA"),
    ("Denmark", "Denmark", "DNK"),
    ("Dominican Republic", "Dominican Republic", "DOM"),
    ("Algeria", "Algeria", "DZA"),
    (None, "East Asia & Pacific (excluding high income)", "EAP"),
    (None, "Early-demographic dividend", "EAR"),
    (None, "East Asia & Pacific", "EAS"),
    (None, "Europe & Central Asia (excluding high income)", "ECA"),
    (None, "Europe & Central Asia", "ECS"),
    ("Ecuador", "Ecuador", "ECU"),
    ("Egypt", "Egypt, Arab Rep.", "EGY"),
    # ("Euro area", "Euro area", "EMU"),
    ("Spain", "Spain", "ESP"),
    ("Estonia", "Estonia", "EST"),
    ("Ethiopia", "Ethiopia", "ETH"),
    ("European Union", "European Union", "EUU"),
    (None, "Fragile and conflict affected situations", "FCS"),
    ("Finland", "Finland", "FIN"),
    ("Fiji", "Fiji", "FJI"),
    ("France", "France", "FRA"),
    ("Faroe Islands", "Faroe Islands", "FRO"),
    ("Federated States of Micronesia", "Micronesia, Fed. Sts.", "FSM"),
    ("Gabon", "Gabon", "GAB"),
    ("United Kingdom", "United Kingdom", "GBR"),
    ("Georgia", "Georgia", "GEO"),
    ("Ghana", "Ghana", "GHA"),
    ("Guinea", "Guinea", "GIN"),
    ("The Gambia", "Gambia, The", "GMB"),
    ("Guinea-Bissau", "Guinea-Bissau", "GNB"),
    ("Equatorial Guinea", "Equatorial Guinea", "GNQ"),
    ("Greece", "Greece", "GRC"),
    ("Grenada", "Grenada", "GRD"),
    ("Greenland", "Greenland", "GRL"),
    ("Guatemala", "Guatemala", "GTM"),
    ("Guam", "Guam", "GUM"),
    ("Guyana", "Guyana", "GUY"),
    (None, "High income", "HIC"),
    ("Hong Kong", "Hong Kong SAR, China", "HKG"),
    ("Honduras", "Honduras", "HND"),
    (None, "Heavily indebted poor countries (HIPC)", "HPC"),
    ("Croatia", "Croatia", "HRV"),
    ("Haiti", "Haiti", "HTI"),
    ("Hungary", "Hungary", "HUN"),
    (None, "IBRD only", "IBD"),
    (None, "IDA & IBRD total", "IBT"),
    (None, "IDA total", "IDA"),
    (None, "IDA blend", "IDB"),
    ("Indonesia", "Indonesia", "IDN"),
    (None, "IDA only", "IDX"),
    ("Isle of Man", "Isle of Man", "IMN"),
    ("India", "India", "IND"),
    ("Republic of Ireland", "Ireland", "IRL"),
    ("Iran", "Iran, Islamic Rep.", "IRN"),
    ("Iraq", "Iraq", "IRQ"),
    ("Iceland", "Iceland", "ISL"),
    ("Israel", "Israel", "ISR"),
    ("Italy", "Italy", "ITA"),
    ("Jamaica", "Jamaica", "JAM"),
    ("Jordan", "Jordan", "JOR"),
    ("Japan", "Japan", "JPN"),
    ("Kazakhstan", "Kazakhstan", "KAZ"),
    ("Kenya", "Kenya", "KEN"),
    ("Kyrgyzstan", "Kyrgyz Republic", "KGZ"),
    ("Cambodia", "Cambodia", "KHM"),
    ("Kiribati", "Kiribati", "KIR"),
    ("Saint Kitts and Nevis", "St. Kitts and Nevis", "KNA"),
    ("South Korea", "Korea, Rep.", "KOR"),
    ("Kuwait", "Kuwait", "KWT"),
    (None, "Latin America & Caribbean (excluding high income)", "LAC"),
    ("Laos", "Lao PDR", "LAO"),
    ("Lebanon", "Lebanon", "LBN"),
    ("Liberia", "Liberia", "LBR"),
    ("Libya", "Libya", "LBY"),
    ("Saint Lucia", "St. Lucia", "LCA"),
    (None, "Latin America & Caribbean", "LCN"),
    (None, "Least developed countries: UN classification", "LDC"),
    (None, "Low income", "LIC"),
    ("Liechtenstein", "Liechtenstein", "LIE"),
    ("Sri Lanka", "Sri Lanka", "LKA"),
    (None, "Lower middle income", "LMC"),
    (None, "Low & middle income", "LMY"),
    ("Lesotho", "Lesotho", "LSO"),
    (None, "Late-demographic dividend", "LTE"),
    ("Lithuania", "Lithuania", "LTU"),
    ("Luxembourg", "Luxembourg", "LUX"),
    ("Latvia", "Latvia", "LVA"),
    ("Macau", "Macao SAR, China", "MAC"),
    ("Morocco", "Morocco", "MAR"),
    ("Monaco", "Monaco", "MCO"),
    ("Moldova", "Moldova", "MDA"),
    ("Madagascar", "Madagascar", "MDG"),
    ("Maldives", "Maldives", "MDV"),
    (None, "Middle East & North Africa", "MEA"),
    ("Mexico", "Mexico", "MEX"),
    ("Marshall Islands", "Marshall Islands", "MHL"),
    (None, "Middle income", "MIC"),
    ("North Macedonia", "North Macedonia", "MKD"),
    ("Mali", "Mali", "MLI"),
    ("Malta", "Malta", "MLT"),
    ("Myanmar", "Myanmar", "MMR"),
    (None, "Middle East & North Africa (excluding high income)", "MNA"),
    ("Montenegro", "Montenegro", "MNE"),
    ("Mongolia", "Mongolia", "MNG"),
    ("Northern Mariana Islands", "Northern Mariana Islands", "MNP"),
    ("Mozambique", "Mozambique", "MOZ"),
    ("Mauritania", "Mauritania", "MRT"),
    ("Mauritius", "Mauritius", "MUS"),
    ("Malawi", "Malawi", "MWI"),
    ("Malaysia", "Malaysia", "MYS"),
    ("North America", "North America", "NAC"),
    ("Namibia", "Namibia", "NAM"),
    ("New Caledonia", "New Caledonia", "NCL"),
    ("Niger", "Niger", "NER"),
    ("Nigeria", "Nigeria", "NGA"),
    ("Nicaragua", "Nicaragua", "NIC"),
    ("Netherlands", "Netherlands", "NLD"),
    ("Norway", "Norway", "NOR"),
    ("Nepal", "Nepal", "NPL"),
    ("Nauru", "Nauru", "NRU"),
    ("New Zealand", "New Zealand", "NZL"),
    ("Organisation for Economic Cooperation and Development", "OECD members", "OED"),
    ("Oman", "Oman", "OMN"),
    (None, "Other small states", "OSS"),
    ("Pakistan", "Pakistan", "PAK"),
    ("Panama", "Panama", "PAN"),
    ("Peru", "Peru", "PER"),
    ("Philippines", "Philippines", "PHL"),
    ("Palau", "Palau", "PLW"),
    ("Papua New Guinea", "Papua New Guinea", "PNG"),
    ("Poland", "Poland", "POL"),
    (None, "Pre-demographic dividend", "PRE"),
    ("Puerto Rico", "Puerto Rico", "PRI"),
    ("Portugal", "Portugal", "PRT"),
    ("Paraguay", "Paraguay", "PRY"),
    ("Palestinian territories", "West Bank and Gaza", "PSE"),
    (None, "Pacific island small states", "PSS"),
    (None, "Post-demographic dividend", "PST"),
    ("Qatar", "Qatar", "QAT"),
    ("Romania", "Romania", "ROU"),
    ("Russia", "Russian Federation", "RUS"),
    ("Rwanda", "Rwanda", "RWA"),
    ("South Asia", "South Asia", "SAS"),
    ("Saudi Arabia", "Saudi Arabia", "SAU"),
    ("Sudan", "Sudan", "SDN"),
    ("Senegal", "Senegal", "SEN"),
    ("Singapore", "Singapore", "SGP"),
    ("Solomon Islands", "Solomon Islands", "SLB"),
    ("Sierra Leone", "Sierra Leone", "SLE"),
    ("El Salvador", "El Salvador", "SLV"),
    ("San Marino", "San Marino", "SMR"),
    ("Somalia", "Somalia", "SOM"),
    ("Serbia", "Serbia", "SRB"),
    (None, "Sub-Saharan Africa (excluding high income)", "SSA"),
    ("South Sudan", "South Sudan", "SSD"),
    ("Sub-Saharan Africa", "Sub-Saharan Africa", "SSF"),
    (None, "Small states", "SST"),
    ("São Tomé and Príncipe", "Sao Tome and Principe", "STP"),
    ("Suriname", "Suriname", "SUR"),
    ("Slovakia", "Slovak Republic", "SVK"),
    ("Slovenia", "Slovenia", "SVN"),
    ("Sweden", "Sweden", "SWE"),
    ("Eswatini", "Eswatini", "SWZ"),
    ("Sint Maarten", "Sint Maarten (Dutch part)", "SXM"),
    ("Seychelles", "Seychelles", "SYC"),
    ("Syria", "Syrian Arab Republic", "SYR"),
    ("Turks and Caicos Islands", "Turks and Caicos Islands", "TCA"),
    ("Chad", "Chad", "TCD"),
    (None, "East Asia & Pacific (IDA & IBRD countries)", "TEA"),
    (None, "Europe & Central Asia (IDA & IBRD countries)", "TEC"),
    ("Togo", "Togo", "TGO"),
    ("Thailand", "Thailand", "THA"),
    ("Tajikistan", "Tajikistan", "TJK"),
    ("Turkmenistan", "Turkmenistan", "TKM"),
    (None, "Latin America & the Caribbean (IDA & IBRD countries)", "TLA"),
    ("East Timor", "Timor-Leste", "TLS"),
    (None, "Middle East & North Africa (IDA & IBRD countries)", "TMN"),
    ("Tonga", "Tonga", "TON"),
    (None, "South Asia (IDA & IBRD)", "TSA"),
    (None, "Sub-Saharan Africa (IDA & IBRD countries)", "TSS"),
    ("Trinidad and Tobago", "Trinidad and Tobago", "TTO"),
    ("Tunisia", "Tunisia", "TUN"),
    ("Turkey", "Turkey", "TUR"),
    ("Tuvalu", "Tuvalu", "TUV"),
    ("Tanzania", "Tanzania", "TZA"),
    ("Uganda", "Uganda", "UGA"),
    ("Ukraine", "Ukraine", "UKR"),
    (None, "Upper middle income", "UMC"),
    ("Uruguay", "Uruguay", "URY"),
    ("United States of America", "United States", "USA"),
    ("Uzbekistan", "Uzbekistan", "UZB"),
    ("Saint Vincent and the Grenadines", "St. Vincent and the Grenadines", "VCT"),
    ("United States Virgin Islands", "Virgin Islands (U.S.)", "VIR"),
    ("Vietnam", "Vietnam", "VNM"),
    ("Vanuatu", "Vanuatu", "VUT"),
    ("World", "World", "WLD"),
    ("Samoa", "Samoa", "WSM"),
    ("Kosovo", "Kosovo", "XKX"),
    ("Yemen", "Yemen, Rep.", "YEM"),
    ("South Africa", "South Africa", "ZAF"),
    ("Zambia", "Zambia", "ZMB"),
    ("Zimbabwe", "Zimbabwe", "ZWE"),
]

WDDS = WikidataDatasource()
WDDS.set_alias("country", "Ireland", "Q27", "Republic of Ireland")
WDDS.set_alias("world", "World", "Q16502", "World")
WDDS.set_alias("country", "China Hong Kong SAR", "Q8646", "Hong Kong")
WDDS.set_alias_code(
    "intergovernmental organization", "OED", "Q8646", "Organisation for Economic Cooperation and Development"
)


@pytest.mark.skipif("CI" in os.environ, reason="Too long for the CI")
@pytest.mark.parametrize("expected,region", BP_DATA)
def test_bp(expected, region):
    if region.startswith("Total "):
        region = region[6:]
    region = region.strip(" #")
    result = WDDS.get_region(region)
    result = None if result is None else result["label"]
    assert result == expected, region


@pytest.mark.skipif("CI" in os.environ, reason="Too long for the CI")
@pytest.mark.parametrize("expected,iso_code,continent,location", WORLD_IN_DATA_DATA)
def test_world_in_data(expected, iso_code, continent, location):
    result = WDDS.get_region(location, iso_code)
    result = None if result is None else result["label"]
    assert result == expected, f"{location}, {iso_code}"


@pytest.mark.skipif("CI" in os.environ, reason="Too long for the CI")
@pytest.mark.parametrize("expected,country_name,country_code", WORLDBANK_DATA)
def test_worldbank(expected, country_name, country_code):
    result = WDDS.get_region(country_name, country_code)
    result = None if result is None else result["label"]
    assert result == expected, f"{country_name}, {country_code}"


@pytest.mark.parametrize(
    "expected,country_name,country_code",
    [
        ("World", "World", None),
        ("Yemen", "Yemen", None),
        ("Yemen", None, "YEM"),
    ],
)
def test_simple(expected, country_name, country_code):
    result = WDDS.get_region(country_name, country_code)
    result = None if result is None else result["label"]
    assert result == expected, f"{country_name}, {country_code}"
