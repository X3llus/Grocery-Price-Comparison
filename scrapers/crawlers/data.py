  # These are the high-level categories that we want to scrape
  # Walmart limits the pages for each of these categories to 25 (60 results per page)
  # If we want to scrape more than 25 pages, we need to use the subcategories
walmart_categories = {
  "preparedMeals": "6000194327356",
  "meat": "6000194327357",
  "fruitsAndVegetables": "6000194327370",
  "deli": "6000194327356",
  "bakery": "6000194327359",
  "dairyAndEggs": "6000194327369",
  "drinks": "6000194326336",
  "frozen": "6000194326337",
  "pantry": "6000194326346",
  "snacksChipsAndCandy": "6000194328523",
  "internationalFoods": "6000195495824",
}

loblaws_categories = {
  "preparedMeals": "27996",
  "meat": "27998",
  "fishAndSeafood": "27999",
  "fruitsAndVegetables": "28000",
  "deli": "28001",
  "bakery": "28002",
  "dairyAndEggs": "28003",
  "drinks": "28004",
  "frozen": "28005",
  "pantry": "28006",
  "naturalFoods": "28189",
  "beerAndWine": "28236",
  "snacksChipsAndCandy": "57025",
  "internationalFoods": "58044",
}


store_locations = [
    {
        "id": 3153,
        "address": {
            "address1": "175 Murphy Rd",
            "city": "Orillia",
            "postalCode": "L3V 0B5"
        }
    },
    {
        "id": 3166,
        "address": {
            "address1": "450 Bayfield St",
            "city": "Barrie",
            "postalCode": "L4M 5A2"
        }
    },
    {
        "id": 3645,
        "address": {
            "address1": "16845 Hwy # 12",
            "city": "Midland",
            "postalCode": "L4R 0A9"
        }
    },
    {
        "id": 3123,
        "address": {
            "address1": "35 Mapleview Dr W",
            "city": "Barrie",
            "postalCode": "L4N 9H5"
        }
    },
    {
        "id": 1012,
        "address": {
            "address1": "23550 Woodbine Ave",
            "city": "Keswick",
            "postalCode": "L4P 0E2"
        }
    },
    {
        "id": 1087,
        "address": {
            "address1": "100 Stonebridge Blvd",
            "city": "Wasaga Beach",
            "postalCode": "L9Z 0C1"
        }
    },
    {
        "id": 1054,
        "address": {
            "address1": "40 Depot Dr Rr7",
            "city": "Bracebridge",
            "postalCode": "P1L 0H1"
        }
    },
    {
        "id": 1101,
        "address": {
            "address1": "545 Holland St W",
            "city": "Bradford",
            "postalCode": "L3Z 0C1"
        }
    },
    {
        "id": 1083,
        "address": {
            "address1": "30 Dunham Dr",
            "city": "Alliston",
            "postalCode": "L9R 0G1"
        }
    },
    {
        "id": 3062,
        "address": {
            "address1": "17940 Yonge St",
            "city": "Newmarket",
            "postalCode": "L3Y 8S4"
        }
    },
    {
        "id": 3653,
        "address": {
            "address1": "6 Welwood Dr",
            "city": "Uxbridge",
            "postalCode": "L9P 1Z7"
        }
    },
    {
        "id": 1039,
        "address": {
            "address1": "10 Cambridge St",
            "city": "Collingwood",
            "postalCode": "L9Y 0A1"
        }
    },
    {
        "id": 5778,
        "address": {
            "address1": "135 First Commerce Dr",
            "city": "Aurora",
            "postalCode": "L4G 0G2"
        }
    },
    {
        "id": 1069,
        "address": {
            "address1": "1535 Hwy 7a",
            "city": "Port Perry",
            "postalCode": "L9L 1B5"
        }
    },
    {
        "id": 1029,
        "address": {
            "address1": "1050 Hoover Pk Dr",
            "city": "Stouffville",
            "postalCode": "L4A 0K2"
        }
    },
    {
        "id": 3195,
        "address": {
            "address1": "1070 Major Mackenzie Dr E",
            "city": "Richmond Hill",
            "postalCode": "L4S 1P3"
        }
    },
    {
        "id": 5743,
        "address": {
            "address1": "111 Howland Dr",
            "city": "Huntsville",
            "postalCode": "P1H 2P4"
        }
    },
    {
        "id": 3053,
        "address": {
            "address1": "5000 Hwy 7",
            "city": "Markham",
            "postalCode": "L3R 4M9"
        }
    },
    {
        "id": 1115,
        "address": {
            "address1": "1900 Major Mackenzie Dr",
            "city": "Vaughan",
            "postalCode": "L6A 4R9"
        }
    },
    {
        "id": 1109,
        "address": {
            "address1": "500 Copper Creek Dr",
            "city": "Markham",
            "postalCode": "L6B 0S1"
        }
    },
    {
        "id": 1095,
        "address": {
            "address1": "3600 Major Mackenzie Dr W",
            "city": "Vaughan",
            "postalCode": "L4H 3T6"
        }
    },
    {
        "id": 1116,
        "address": {
            "address1": "255 Silver Linden Dr",
            "city": "Richmond Hill",
            "postalCode": "L4B 4V5"
        }
    },
    {
        "id": 5742,
        "address": {
            "address1": "150 Mcewan Dr E",
            "city": "Bolton",
            "postalCode": "L7E 2Y3"
        }
    },
    {
        "id": 3113,
        "address": {
            "address1": "4100 Baldwin St S",
            "city": "Whitby",
            "postalCode": "L1R 3H8"
        }
    },
    {
        "id": 1080,
        "address": {
            "address1": "5995 Steeles Ave E",
            "city": "Scarborough",
            "postalCode": "M1V 5P7"
        }
    },
    {
        "id": 3161,
        "address": {
            "address1": "1471 Harmony Rd N",
            "city": "Oshawa",
            "postalCode": "L1H 7K5"
        }
    },
    {
        "id": 5831,
        "address": {
            "address1": "700 Centre St",
            "city": "Thornhill",
            "postalCode": "L4J 0A7"
        }
    },
    {
        "id": 3001,
        "address": {
            "address1": "270 Kingston Rd E R R # 1",
            "city": "Ajax",
            "postalCode": "L1Z 1G1"
        }
    },
    {
        "id": 3186,
        "address": {
            "address1": "1899 Brock Rd",
            "city": "Pickering",
            "postalCode": "L1V 4H7"
        }
    },
    {
        "id": 3174,
        "address": {
            "address1": "670 Applewood Crescent",
            "city": "Vaughan",
            "postalCode": "L4K 4B4"
        }
    },
    {
        "id": 3142,
        "address": {
            "address1": "95 1st St",
            "city": "Orangeville",
            "postalCode": "L9W 2E8"
        }
    },
    {
        "id": 3111,
        "address": {
            "address1": "799 Milner Ave",
            "city": "Scarborough",
            "postalCode": "M1B 3C3"
        }
    },
    {
        "id": 1023,
        "address": {
            "address1": "1 Pine Dr",
            "city": "Parry Sound",
            "postalCode": "P2A 3C3"
        }
    },
    {
        "id": 1056,
        "address": {
            "address1": "680 Laval Dr",
            "city": "Oshawa",
            "postalCode": "L1J 0B5"
        }
    },
    {
        "id": 1081,
        "address": {
            "address1": "8300 Hwy 27",
            "city": "Woodbridge",
            "postalCode": "L4H 0R9"
        }
    },
    {
        "id": 3071,
        "address": {
            "address1": "1002 Chemong Rd",
            "city": "Peterborough",
            "postalCode": "K9H 7E2"
        }
    },
    {
        "id": 3635,
        "address": {
            "address1": "300 Borough Dr",
            "city": "Scarborough",
            "postalCode": "M1P 4P5"
        }
    },
    {
        "id": 1162,
        "address": {
            "address1": "950 Lansdowne St W",
            "city": "Peterborough",
            "postalCode": "K9J 1Z9"
        }
    },
    {
        "id": 1139,
        "address": {
            "address1": "3757 Keele St",
            "city": "Toronto",
            "postalCode": "M3J 1N4"
        }
    },
    {
        "id": 1120,
        "address": {
            "address1": "5085 Mayfield Rd",
            "city": "Brampton",
            "postalCode": "L6R 3S9"
        }
    },
    {
        "id": 1001,
        "address": {
            "address1": "2320 Highway 2",
            "city": "Bowmanville",
            "postalCode": "L1C 3K7"
        }
    },
    {
        "id": 1117,
        "address": {
            "address1": "3132 Eglinton Ave E",
            "city": "Scarborough",
            "postalCode": "M1J 2H1"
        }
    },
    {
        "id": 3135,
        "address": {
            "address1": "30 Coventry Rd",
            "city": "Brampton",
            "postalCode": "L6T 5P9"
        }
    },
    {
        "id": 3159,
        "address": {
            "address1": "1900 Eglinton Ave E",
            "city": "Scarborough",
            "postalCode": "M1L 2L9"
        }
    },
    {
        "id": 3740,
        "address": {
            "address1": "2245 Islington Ave",
            "city": "Toronto",
            "postalCode": "M9W 3W6"
        }
    },
    {
        "id": 4107,
        "address": {
            "address1": "2625E Weston Road",
            "city": "North York ",
            "postalCode": "M9N 3X2"
        }
    },
    {
        "id": 3105,
        "address": {
            "address1": "1305 Lawrence Ave W",
            "city": "Toronto",
            "postalCode": "M6L 1A5"
        }
    },
    {
        "id": 4008,
        "address": {
            "address1": "120 Eglinton Ave E",
            "city": "Toronto",
            "postalCode": "M4P 1A6"
        }
    },
    {
        "id": 3130,
        "address": {
            "address1": "50 Quarry Edge Dr",
            "city": "Brampton",
            "postalCode": "L6V 4K2"
        }
    },
    {
        "id": 4013,
        "address": {
            "address1": "609 Church",
            "city": "Toronto",
            "postalCode": "M4Y 2E6"
        }
    },
    {
        "id": 1004,
        "address": {
            "address1": "2525 St Clair Ave W",
            "city": "Toronto",
            "postalCode": "M6N 4Z5"
        }
    },
    {
        "id": 4006,
        "address": {
            "address1": "453 Parliament Street",
            "city": "Toronto",
            "postalCode": "M5A 3A3"
        }
    },
    {
        "id": 4001,
        "address": {
            "address1": "21/25 Carlton St",
            "city": "Toronto",
            "postalCode": "M5B 1L3"
        }
    },
    {
        "id": 1188,
        "address": {
            "address1": "15 Resolution Dr",
            "city": "Brampton",
            "postalCode": "L6W 0A6"
        }
    },
    {
        "id": 3106,
        "address": {
            "address1": "900 Dufferin St",
            "city": "Toronto",
            "postalCode": "M6H 4A9"
        }
    },
    {
        "id": 4002,
        "address": {
            "address1": "629 Eastern Avenue",
            "city": "Toronto",
            "postalCode": "M4M 1E3"
        }
    },
    {
        "id": 4018,
        "address": {
            "address1": "250 University Ave",
            "city": "Toronto",
            "postalCode": "M5H 3E5"
        }
    },
    {
        "id": 4017,
        "address": {
            "address1": "53 Yonge St",
            "city": "Toronto",
            "postalCode": "M5E 1J3"
        }
    },
    {
        "id": 4014,
        "address": {
            "address1": "93 Peter St",
            "city": "Toronto",
            "postalCode": "M5V 0P1"
        }
    },
    {
        "id": 4012,
        "address": {
            "address1": "531 Adelaide St W",
            "city": "Toronto",
            "postalCode": "M5V 1T6"
        }
    },
    {
        "id": 4011,
        "address": {
            "address1": "68 Abell St",
            "city": "Toronto",
            "postalCode": "M6J 0B1"
        }
    },
    {
        "id": 4000,
        "address": {
            "address1": "15/21 Iceboat Terrace",
            "city": "Toronto",
            "postalCode": "M5V 4A9"
        }
    },
    {
        "id": 4007,
        "address": {
            "address1": "228 Queens Quay W",
            "city": "Toronto",
            "postalCode": "M5J 1A1"
        }
    },
    {
        "id": 1079,
        "address": {
            "address1": "9455 Mississauga Rd",
            "city": "Brampton",
            "postalCode": "L6X 0Z8"
        }
    },
    {
        "id": 3031,
        "address": {
            "address1": "165 N Queen St",
            "city": "Etobicoke",
            "postalCode": "M9C 1A7"
        }
    },
    {
        "id": 1126,
        "address": {
            "address1": "1500 Dundas St E",
            "city": "Mississauga",
            "postalCode": "L4X 1L4"
        }
    },
    {
        "id": 3034,
        "address": {
            "address1": "300 Guelph St",
            "city": "Georgetown",
            "postalCode": "L7G 4B1"
        }
    },
    {
        "id": 1061,
        "address": {
            "address1": "800 Matheson Blvd W",
            "city": "Mississauga",
            "postalCode": "L5V 2N6"
        }
    },
    {
        "id": 3055,
        "address": {
            "address1": "100 City Centre Dr",
            "city": "Mississauga",
            "postalCode": "L5B 2G7"
        }
    },
    {
        "id": 8123,
        "address": {
            "address1": "1940 Argentia Road",
            "city": "Mississauga",
            "postalCode": "L5N 5N1"
        }
    },
    {
        "id": 3067,
        "address": {
            "address1": "1555 18th Ave E",
            "city": "Owen Sound",
            "postalCode": "N4K 6Y3"
        }
    },
    {
        "id": 3054,
        "address": {
            "address1": "3155 Argentia Rd",
            "city": "Meadowvale",
            "postalCode": "L5N 8E1"
        }
    },
    {
        "id": 1211,
        "address": {
            "address1": "5100 Erin Mills Pky",
            "city": "Mississauga West",
            "postalCode": "L5M 4Z5"
        }
    },
    {
        "id": 3654,
        "address": {
            "address1": "2160 Burnhamthorpe Rd W",
            "city": "Mississauga",
            "postalCode": "L5L 5Z5"
        }
    },
    {
        "id": 3133,
        "address": {
            "address1": "73 Strathy Rd",
            "city": "Cobourg",
            "postalCode": "K9A 5W8"
        }
    },
    {
        "id": 1000,
        "address": {
            "address1": "1280 Steeles Ave E",
            "city": "Milton",
            "postalCode": "L9T 6R1"
        }
    },
    {
        "id": 1130,
        "address": {
            "address1": "801 St David St N",
            "city": "Fergus",
            "postalCode": "N1M 2L1"
        }
    },
    {
        "id": 3064,
        "address": {
            "address1": "234 Hays Blvd",
            "city": "Oakville",
            "postalCode": "L6H 6M4"
        }
    },
    {
        "id": 4009,
        "address": {
            "address1": "1410 Trafalgar Road",
            "city": "Toronto",
            "postalCode": "L6H 2L1"
        }
    },
    {
        "id": 3129,
        "address": {
            "address1": "1100 10th St",
            "city": "Hanover",
            "postalCode": "N4N 3B8"
        }
    },
    {
        "id": 3144,
        "address": {
            "address1": "11 Woodlawn Rd W",
            "city": "Guelph",
            "postalCode": "N1H 1G8"
        }
    },
    {
        "id": 1199,
        "address": {
            "address1": "175 Stone Rd W",
            "city": "Guelph",
            "postalCode": "N1G 5L4"
        }
    },
    {
        "id": 3170,
        "address": {
            "address1": "4515 Dundas St",
            "city": "Burlington",
            "postalCode": "L7M 5B4"
        }
    },
    {
        "id": 3141,
        "address": {
            "address1": "2065 Fairview St",
            "city": "Burlington",
            "postalCode": "L7R 0B4"
        }
    },
    {
        "id": 1107,
        "address": {
            "address1": "90 Dundas St E",
            "city": "Waterdown",
            "postalCode": "L9H 0C2"
        }
    },
    {
        "id": 3152,
        "address": {
            "address1": "22 Pinebush Rd",
            "city": "Cambridge",
            "postalCode": "N1R 8K5"
        }
    },
    {
        "id": 3156,
        "address": {
            "address1": "335 Farmers Market Rd Unit 101",
            "city": "Waterloo",
            "postalCode": "N2V 0A4"
        }
    },
    {
        "id": 1156,
        "address": {
            "address1": "70 Bridgeport Rd E",
            "city": "Waterloo",
            "postalCode": "N2J 2J9"
        }
    },
    {
        "id": 3045,
        "address": {
            "address1": "2960 Kingsway Dr",
            "city": "Kitchener",
            "postalCode": "N2C 1X1"
        }
    },
    {
        "id": 1121,
        "address": {
            "address1": "1115 Barton St E",
            "city": "Hamilton",
            "postalCode": "L8H 2V2"
        }
    },
    {
        "id": 3096,
        "address": {
            "address1": "510 Centennial Pkwy N",
            "city": "Hamilton",
            "postalCode": "L8E 0G2"
        }
    },
    {
        "id": 1059,
        "address": {
            "address1": "5122 On-21",
            "city": "Port Elgin",
            "postalCode": "N0H 2C0"
        }
    },
    {
        "id": 1160,
        "address": {
            "address1": "600 Mitchell Rd S",
            "city": "Listowel",
            "postalCode": "N4W 3T1"
        }
    },
    {
        "id": 3037,
        "address": {
            "address1": "675 Upper James St",
            "city": "Hamilton",
            "postalCode": "L9C 2Z5"
        }
    },
    {
        "id": 3178,
        "address": {
            "address1": "470 2nd Dug Hill Rd",
            "city": "Trenton",
            "postalCode": "K8V 5P7"
        }
    },
    {
        "id": 1007,
        "address": {
            "address1": "1400 Ottawa St S",
            "city": "Kitchener",
            "postalCode": "N2E 4E2"
        }
    },
    {
        "id": 1111,
        "address": {
            "address1": "100 The Boardwalk",
            "city": "Kitchener",
            "postalCode": "N2N 0B1"
        }
    },
    {
        "id": 3088,
        "address": {
            "address1": "525 Welland Ave",
            "city": "St. Catharines",
            "postalCode": "L2M 6P3"
        }
    },
    {
        "id": 1042,
        "address": {
            "address1": "2190 Rymal Rd E",
            "city": "Hannon",
            "postalCode": "L0R 1P0"
        }
    },
    {
        "id": 3172,
        "address": {
            "address1": "420 Vansickle Rd",
            "city": "St. Catharines",
            "postalCode": "L2S 0C7"
        }
    },
    {
        "id": 3127,
        "address": {
            "address1": "1051 Garner Rd W",
            "city": "Ancaster",
            "postalCode": "L9G 3K9"
        }
    },
    {
        "id": 1164,
        "address": {
            "address1": "221 Glendale Ave,",
            "city": "St. Catharines",
            "postalCode": "L2T 2K9"
        }
    },
    {
        "id": 3122,
        "address": {
            "address1": "274 Millennium Pky",
            "city": "Belleville",
            "postalCode": "K8N 4Z5"
        }
    },
    {
        "id": 3005,
        "address": {
            "address1": "1-300 King George Rd",
            "city": "Brantford",
            "postalCode": "N3R 5L7"
        }
    },
    {
        "id": 3160,
        "address": {
            "address1": "7481 Oakwood Dr",
            "city": "Niagara Falls",
            "postalCode": "L2G 0J5"
        }
    },
    {
        "id": 3110,
        "address": {
            "address1": "102 Primeway Dr",
            "city": "Welland",
            "postalCode": "L3B 0A1"
        }
    },
    {
        "id": 1125,
        "address": {
            "address1": "920 Ontario St",
            "city": "Stratford",
            "postalCode": "N5A 3K1"
        }
    },
    {
        "id": 3063,
        "address": {
            "address1": "1500 Fisher St",
            "city": "North Bay",
            "postalCode": "P1B 2H3"
        }
    },
    {
        "id": 3649,
        "address": {
            "address1": "750 Garrison Rd",
            "city": "Fort Erie",
            "postalCode": "L2A 1N7"
        }
    },
    {
        "id": 3120,
        "address": {
            "address1": "499 Norwich Ave",
            "city": "Woodstock",
            "postalCode": "N4S 9A2"
        }
    },
    {
        "id": 1041,
        "address": {
            "address1": "89 Jim Kimmett Blvd",
            "city": "Napanee",
            "postalCode": "K7R 3L1"
        }
    },
    {
        "id": 3126,
        "address": {
            "address1": "35400 Huron Rd Rr2",
            "city": "Goderich",
            "postalCode": "N7A 3X8"
        }
    },
    {
        "id": 5752,
        "address": {
            "address1": "160 Queensway E",
            "city": "Simcoe",
            "postalCode": "N3Y 0A8"
        }
    },
    {
        "id": 3049,
        "address": {
            "address1": "330 Clarke Rd",
            "city": "E. London",
            "postalCode": "N5W 6G4"
        }
    },
    {
        "id": 3171,
        "address": {
            "address1": "1108 Pembroke St E",
            "city": "Pembroke",
            "postalCode": "K8A 8P7"
        }
    },
    {
        "id": 3043,
        "address": {
            "address1": "1130 Midland Ave",
            "city": "Kingston",
            "postalCode": "K7P 2X9"
        }
    },
    {
        "id": 3050,
        "address": {
            "address1": "1280 Fanshawe Pk Rd W",
            "city": "London",
            "postalCode": "N6G 5B1"
        }
    },
    {
        "id": 3051,
        "address": {
            "address1": "1105 Wellington Rd",
            "city": "London",
            "postalCode": "N6E 1V4"
        }
    },
    {
        "id": 1105,
        "address": {
            "address1": "2416 Long Lake Rd",
            "city": "Sudbury",
            "postalCode": "P3E 0C5"
        }
    },
    {
        "id": 3078,
        "address": {
            "address1": "980 O'brien Rd",
            "city": "Renfrew",
            "postalCode": "K7V 0B4"
        }
    },
    {
        "id": 3097,
        "address": {
            "address1": "1349 Lasalle Blvd",
            "city": "Sudbury",
            "postalCode": "P3A 1Z2"
        }
    },
    {
        "id": 3197,
        "address": {
            "address1": "1063 Talbot St Unit # 60",
            "city": "St. Thomas",
            "postalCode": "N5P 1G4"
        }
    },
    {
        "id": 1038,
        "address": {
            "address1": "150 Carroll St E Rr 1",
            "city": "Strathroy",
            "postalCode": "N7G 4G2"
        }
    },
    {
        "id": 1075,
        "address": {
            "address1": "450 Mcneely Ave",
            "city": "Carleton Place",
            "postalCode": "K7C 0A6"
        }
    },
    {
        "id": 5811,
        "address": {
            "address1": "114 Lombard St",
            "city": "Smiths Falls",
            "postalCode": "K7A 5B8"
        }
    },
    {
        "id": 3134,
        "address": {
            "address1": "500 Earl Grey Dr",
            "city": "Kanata",
            "postalCode": "K2T 1B6"
        }
    },
    {
        "id": 1118,
        "address": {
            "address1": "5357 Fernbank Rd",
            "city": "Stittsville",
            "postalCode": "K2S 0T7"
        }
    },
    {
        "id": 3082,
        "address": {
            "address1": "1444 Quinn Dr",
            "city": "Sarnia",
            "postalCode": "N7S 6M8"
        }
    },
    {
        "id": 3006,
        "address": {
            "address1": "1942 Parkedale Ave",
            "city": "Brockville",
            "postalCode": "K6V 7N4"
        }
    },
    {
        "id": 3066,
        "address": {
            "address1": "100 Bayshore Dr",
            "city": "Ottawa",
            "postalCode": "K2B 8C1"
        }
    },
    {
        "id": 3638,
        "address": {
            "address1": "3651 Strandherd Dr",
            "city": "Barrhaven",
            "postalCode": "K2J 4G8"
        }
    },
    {
        "id": 3143,
        "address": {
            "address1": "35 Boul Du Plateau",
            "city": "Hull",
            "postalCode": "J9A 3G1"
        }
    },
    {
        "id": 1110,
        "address": {
            "address1": "1375 Baseline Rd",
            "city": "Ottawa",
            "postalCode": "K2C 3G1"
        }
    },
    {
        "id": 1047,
        "address": {
            "address1": "340 Colonnade Dr",
            "city": "Kemptville",
            "postalCode": "K0G 1J0"
        }
    },
    {
        "id": 1190,
        "address": {
            "address1": "1-425 Boul Saint Joseph",
            "city": "Hull",
            "postalCode": "J8Y 3Z9"
        }
    },
    {
        "id": 1086,
        "address": {
            "address1": "51 De La Gappe Blvd",
            "city": "Gatineau",
            "postalCode": "J8T 0B5"
        }
    },
    {
        "id": 1200,
        "address": {
            "address1": "2277 Riverside Dr",
            "city": "Ottawa",
            "postalCode": "K1H 7X6"
        }
    },
    {
        "id": 3131,
        "address": {
            "address1": "2210 Bank St",
            "city": "Ottawa",
            "postalCode": "K1V 1J5"
        }
    },
    {
        "id": 1031,
        "address": {
            "address1": "450 Terminal Ave",
            "city": "Ottawa",
            "postalCode": "K1G 0Z3"
        }
    },
    {
        "id": 3125,
        "address": {
            "address1": "640 Blvd Maloney W",
            "city": "Gatineau",
            "postalCode": "J8T 8K7"
        }
    },
    {
        "id": 1158,
        "address": {
            "address1": "1980 Ogilvie Rd",
            "city": "Gloucester",
            "postalCode": "K1J 9L3"
        }
    },
    {
        "id": 3065,
        "address": {
            "address1": "3900 Innes Rd",
            "city": "Orleans",
            "postalCode": "K1W 1K9"
        }
    },
    {
        "id": 3128,
        "address": {
            "address1": "133 Hwy # 11",
            "city": "Temiskaming Shores",
            "postalCode": "P0J 1P0"
        }
    },
    {
        "id": 1064,
        "address": {
            "address1": "60 Mcnaughton Ave Unit # 16",
            "city": "Wallaceburg",
            "postalCode": "N8A 1R9"
        }
    },
    {
        "id": 3016,
        "address": {
            "address1": "881 St Clair St",
            "city": "Chatham",
            "postalCode": "N7L 0E9"
        }
    },
    {
        "id": 1060,
        "address": {
            "address1": "3001 Richelieu St",
            "city": "Rockland",
            "postalCode": "K4K 0B5"
        }
    },
    {
        "id": 3020,
        "address": {
            "address1": "420 Ninth St W",
            "city": "Cornwall",
            "postalCode": "K6J 0B3"
        }
    },
    {
        "id": 3115,
        "address": {
            "address1": "7100 Tecumseh Rd E",
            "city": "Windsor",
            "postalCode": "N8T 1E6"
        }
    },
    {
        "id": 3164,
        "address": {
            "address1": "304 Erie St S",
            "city": "Leamington",
            "postalCode": "N8H 3C5"
        }
    },
    {
        "id": 3114,
        "address": {
            "address1": "3120 Dougall Ave",
            "city": "Windsor",
            "postalCode": "N9E 1S7"
        }
    },
    {
        "id": 1159,
        "address": {
            "address1": "1550 Cameron St",
            "city": "Hawkesbury",
            "postalCode": "K6A 3S5"
        }
    },
    {
        "id": 3136,
        "address": {
            "address1": "275 Blvd Rideau",
            "city": "Rouyn-noranda",
            "postalCode": "J9X 5Y6"
        }
    },
    {
        "id": 3139,
        "address": {
            "address1": "1855 3e Av",
            "city": "Val-d'or",
            "postalCode": "J9P 7A9"
        }
    },
    {
        "id": 1072,
        "address": {
            "address1": "400 Sandwich St S",
            "city": "Amherstburg",
            "postalCode": "N9V 3L4"
        }
    },
    {
        "id": 3132,
        "address": {
            "address1": "480 Av Bethany",
            "city": "Lachute",
            "postalCode": "J8H 4H5"
        }
    },
    {
        "id": 3639,
        "address": {
            "address1": "2050 Boul Monseigneur Langlois",
            "city": "Salaberry-de-valleyfield",
            "postalCode": "J6S 5R1"
        }
    },
    {
        "id": 1057,
        "address": {
            "address1": "3050 Boul De La Gare",
            "city": "Vaudreuil-dorion",
            "postalCode": "J7V 0H1"
        }
    },
    {
        "id": 1020,
        "address": {
            "address1": "400 Rue Laverdure",
            "city": "Sainte-agathe-des-monts",
            "postalCode": "J8C 0A2"
        }
    },
    {
        "id": 3155,
        "address": {
            "address1": "446 Great Northern Rd",
            "city": "Sault Ste. Marie",
            "postalCode": "P6B 4Z9"
        }
    },
    {
        "id": 3190,
        "address": {
            "address1": "1030 Boul Du Grand Heron",
            "city": "Saint-jerome",
            "postalCode": "J7Y 5K8"
        }
    },
    {
        "id": 3089,
        "address": {
            "address1": "764 Arthur Sauve Boul",
            "city": "Saint-eustache",
            "postalCode": "J7R 4K3"
        }
    },
    {
        "id": 3044,
        "address": {
            "address1": "17000 Rte Transcanadienne",
            "city": "Kirkland",
            "postalCode": "H9J 2M5"
        }
    },
    {
        "id": 1185,
        "address": {
            "address1": "1333 Michele-bohec Blvd",
            "city": "Blainville",
            "postalCode": "J7C 0M4"
        }
    },
    {
        "id": 1202,
        "address": {
            "address1": "195 Boul Hymus",
            "city": "Pointe-claire",
            "postalCode": "H9R 1E9"
        }
    },
    {
        "id": 1132,
        "address": {
            "address1": "250 Boul Briseboise",
            "city": "Chateauguay",
            "postalCode": "J6K 0H5"
        }
    },
    {
        "id": 3104,
        "address": {
            "address1": "1870 Riverside Dr Rr 2",
            "city": "Timmins",
            "postalCode": "P4R 1N7"
        }
    },
    {
        "id": 3080,
        "address": {
            "address1": "401 Boul Labelle",
            "city": "Rosemere",
            "postalCode": "J7A 3T2"
        }
    },
    {
        "id": 3189,
        "address": {
            "address1": "700 Autoroute Chomedey Ouest",
            "city": "Laval",
            "postalCode": "H7X 3S9"
        }
    },
    {
        "id": 3047,
        "address": {
            "address1": "2075 Boul Chomedey",
            "city": "Laval",
            "postalCode": "H7T 0G5"
        }
    },
    {
        "id": 1189,
        "address": {
            "address1": "3820 De La Cote Vertu Blvd",
            "city": "St-laurent",
            "postalCode": "H4R 1P8"
        }
    },
    {
        "id": 1032,
        "address": {
            "address1": "5205 Blvd Robert Bourassa",
            "city": "Laval",
            "postalCode": "H7E 0A3"
        }
    },
    {
        "id": 3165,
        "address": {
            "address1": "5400 Rue Jean-talon O",
            "city": "Montreal",
            "postalCode": "H4P 2T5"
        }
    },
    {
        "id": 1170,
        "address": {
            "address1": "6700 Ch De La Cote-des-neiges",
            "city": "Montreal",
            "postalCode": "H3S 2B2"
        }
    },
    {
        "id": 3046,
        "address": {
            "address1": "6797 Blvd Newman",
            "city": "Lasalle",
            "postalCode": "H8N 3E4"
        }
    },
    {
        "id": 3642,
        "address": {
            "address1": "500 Voie De La Desserte De La Route 132",
            "city": "Saint-constant",
            "postalCode": "J5A 2S5"
        }
    },
    {
        "id": 3656,
        "address": {
            "address1": "6140 Boul Henri-bourassa E",
            "city": "Montreal-nord",
            "postalCode": "H1G 5X3"
        }
    },
    {
        "id": 1183,
        "address": {
            "address1": "7600 Boul Viau",
            "city": "Saint-leonard",
            "postalCode": "H1S 2P3"
        }
    },
    {
        "id": 4016,
        "address": {
            "address1": "1692 Mount-Royale Ave E",
            "city": "Montreal",
            "postalCode": "H2J 1Z5"
        }
    },
    {
        "id": 3094,
        "address": {
            "address1": "7445 Boul Langelier",
            "city": "Saint-leonard",
            "postalCode": "H1S 1V6"
        }
    },
    {
        "id": 3149,
        "address": {
            "address1": "155 Montee Masson",
            "city": "Mascouche",
            "postalCode": "J7K 3B4"
        }
    },
    {
        "id": 1203,
        "address": {
            "address1": "201 Rue Strasbourg",
            "city": "Candiac",
            "postalCode": "J5R 0B4"
        }
    },
    {
        "id": 3052,
        "address": {
            "address1": "1999 Boul Roland-therrien",
            "city": "Longueuil",
            "postalCode": "J4N 1A3"
        }
    },
    {
        "id": 3007,
        "address": {
            "address1": "9000 Blvd Leduc",
            "city": "Brossard",
            "postalCode": "J4Y 0E6"
        }
    },
    {
        "id": 1085,
        "address": {
            "address1": "1001 Rue Des Migrateurs",
            "city": "Terrebonne",
            "postalCode": "J6V 0A8"
        }
    },
    {
        "id": 3079,
        "address": {
            "address1": "100 Boul Brien",
            "city": "Repentigny",
            "postalCode": "J6A 5N4"
        }
    },
    {
        "id": 3140,
        "address": {
            "address1": "1475 Boul St Bruno",
            "city": "Saint-bruno",
            "postalCode": "J3V 6J1"
        }
    },
    {
        "id": 3090,
        "address": {
            "address1": "100 Boul Omer-marcil",
            "city": "St-jean-sur-richelieu",
            "postalCode": "J2W 2X2"
        }
    },
    {
        "id": 3039,
        "address": {
            "address1": "1505 Boul Firestone",
            "city": "Joliette",
            "postalCode": "J6E 9E5"
        }
    },
    {
        "id": 3137,
        "address": {
            "address1": "5950 Rue Martineau",
            "city": "Saint-hyacinthe",
            "postalCode": "J2R 2H6"
        }
    },
    {
        "id": 1174,
        "address": {
            "address1": "450 Boul Poliquin",
            "city": "Sorel-tracy",
            "postalCode": "J3P 7R5"
        }
    },
    {
        "id": 5839,
        "address": {
            "address1": "1770 Rue Du Sud",
            "city": "Cowansville",
            "postalCode": "J2K 3G8"
        }
    },
    {
        "id": 3035,
        "address": {
            "address1": "75 Simonds St N",
            "city": "Granby",
            "postalCode": "J2J 2S3"
        }
    },
    {
        "id": 3023,
        "address": {
            "address1": "1205 Boul Rene-levesque",
            "city": "Drummondville",
            "postalCode": "J2C 7V4"
        }
    },
    {
        "id": 3647,
        "address": {
            "address1": "1600 Blvd Royal",
            "city": "Shawinigan",
            "postalCode": "G9N 8S8"
        }
    },
    {
        "id": 3108,
        "address": {
            "address1": "4520 Boul Des Recollets",
            "city": "Trois-rivieres",
            "postalCode": "G9A 4N2"
        }
    },
    {
        "id": 3041,
        "address": {
            "address1": "350 Government Rd E",
            "city": "Kapuskasing",
            "postalCode": "P5N 2X7"
        }
    },
    {
        "id": 1076,
        "address": {
            "address1": "1935 Sherbrooke St",
            "city": "Magog",
            "postalCode": "J1X 2T5"
        }
    },
    {
        "id": 3086,
        "address": {
            "address1": "4050 Boul Josaphat-rancourt",
            "city": "Sherbrooke",
            "postalCode": "J1L 3C6"
        }
    },
    {
        "id": 3739,
        "address": {
            "address1": "110 Blvd Arthabaska O",
            "city": "Victoriaville",
            "postalCode": "G6S 0P2"
        }
    },
    {
        "id": 5832,
        "address": {
            "address1": "1025 Boul Frontenac E",
            "city": "Thetford Mines",
            "postalCode": "G6G 6S7"
        }
    },
    {
        "id": 3146,
        "address": {
            "address1": "1470 Av Jules-verne",
            "city": "Sainte-foy",
            "postalCode": "G2G 2R5"
        }
    },
    {
        "id": 1045,
        "address": {
            "address1": "700 Rue De La Concorde",
            "city": "Saint-romuald",
            "postalCode": "G6W 8A8"
        }
    },
    {
        "id": 1212,
        "address": {
            "address1": "2700 Boul Laurier",
            "city": "Quebec City",
            "postalCode": "G1V 2L8"
        }
    },
    {
        "id": 3074,
        "address": {
            "address1": "1700 Boul Lebourgneuf",
            "city": "Quebec City",
            "postalCode": "G2K 2M4"
        }
    },
    {
        "id": 1019,
        "address": {
            "address1": "3130 Rue Laval",
            "city": "Lac-megantic",
            "postalCode": "G6B 1A4"
        }
    },
    {
        "id": 1201,
        "address": {
            "address1": "550 Boul Wilfrid-hamel",
            "city": "Quebec City",
            "postalCode": "G1M 2S6"
        }
    },
    {
        "id": 3148,
        "address": {
            "address1": "1200 Boul Alphonse-desjardins",
            "city": "Levis",
            "postalCode": "G6V 6Y8"
        }
    },
    {
        "id": 3646,
        "address": {
            "address1": "224 Joseph Casavant Ave",
            "city": "Quebec City",
            "postalCode": "G1C 7Z3"
        }
    },
    {
        "id": 1040,
        "address": {
            "address1": "750 107e Rue",
            "city": "Saint-georges",
            "postalCode": "G5Y 0A1"
        }
    },
    {
        "id": 5795,
        "address": {
            "address1": "1755 Ave Du Pont S",
            "city": "Alma",
            "postalCode": "G8B 7W7"
        }
    },
    {
        "id": 3017,
        "address": {
            "address1": "1451 Boul Talbot",
            "city": "Chicoutimi",
            "postalCode": "G7H 5N8"
        }
    },
    {
        "id": 1173,
        "address": {
            "address1": "161 Route 230 Ouest Unit 400",
            "city": "La Pocatiere",
            "postalCode": "G0R 1Z0"
        }
    },
    {
        "id": 3655,
        "address": {
            "address1": "100 Rue Des Cerisiers",
            "city": "Riviere-du-loup",
            "postalCode": "G5R 6E8"
        }
    },
    {
        "id": 3124,
        "address": {
            "address1": "777 Memorial Ave",
            "city": "Thunder Bay",
            "postalCode": "P7B 3Z7"
        }
    },
    {
        "id": 1166,
        "address": {
            "address1": "1020 Dawson Rd",
            "city": "Thunder Bay",
            "postalCode": "P7B 1K6"
        }
    },
    {
        "id": 1033,
        "address": {
            "address1": "805 Victoria St",
            "city": "Edmundston",
            "postalCode": "E3V 3T3"
        }
    },
    {
        "id": 3198,
        "address": {
            "address1": "415 Montee Industrielle-et-commerciale",
            "city": "Rimouski",
            "postalCode": "G5M 1Y1"
        }
    },
    {
        "id": 1043,
        "address": {
            "address1": "430 Connell St",
            "city": "Woodstock",
            "postalCode": "E7M 5R5"
        }
    },
    {
        "id": 1013,
        "address": {
            "address1": "494 Ch Madawaska",
            "city": "Grand Falls",
            "postalCode": "E3Y 1A3"
        }
    },
    {
        "id": 3002,
        "address": {
            "address1": "630 Boul Lafleche",
            "city": "Baie-comeau",
            "postalCode": "G5C 2Y3"
        }
    }
]