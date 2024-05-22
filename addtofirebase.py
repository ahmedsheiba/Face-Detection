import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-recognition-95fc2-default-rtdb.firebaseio.com/"
})

ref =db.reference('students')

data={
    "3032":{
        "name":"abdo shadwan",
        "dep":"IT",
        "number":"3032",
    },
    "3159":{
        "name":"abdelsalam",
        "dep":"CS",
        "number":"3159",
    },
      "3151":{
        "name":"abdelrhman abu zied",
        "dep":"CS",
        "number":"3151",
    },
          "3041":{
        "name":"ali ayman",
        "dep":"IT",
        "number":"3041",
    },
          "3007":{
        "name":"ahmed samir",
        "dep":"IT",
        "number":"3007",
    },
          "3109":{
        "name":"ahmed mansour",
        "dep":"CS",
        "number":"3109",
    },
          "3152":{
        "name":"abdelrhman ahmed",
        "dep":"",
        "number":"3152",
    },
          "3008":{
        "name":"ahmed saleh",
        "dep":"IT",
        "number":"3008",
    },
          "3120":{
        "name":"Basmala Abu zeid",
        "dep":"CS",
        "number":"3120",
    },
          "3030":{
        "name":"abdelhamid essam",
        "dep":"IT",
        "number":"3030",
    },
          "3114":{
        "name":"eslam emad",
        "dep":"CS",
        "number":"3114",
    },
          "3179":{
        "name":"mohamed wael",
        "dep":"CS",
        "number":"3179",
    },
          "3050":{
        "name":"farah mohamed",
        "dep":"IT",
        "number":"3050",
    },
          "3016":{
        "name":"alfred ebrahim",
        "dep":"IT",
        "number":"3016",
    },
          "3169":{
        "name":"alaa salem",
        "dep":"CS",
        "number":"3169",
    },
          "3203":{
        "name":"yosef mohamed",
        "dep":"CS",
        "number":"3203",
    },
          "3163":{
        "name":"abdelkarem yones",
        "dep":"CS",
        "number":"3163",
    },
          "3189":{
        "name":"moamen ayman",
        "dep":"CS",
        "number":"3189",
    },
          "3020":{
        "name":"hossam hassan",
        "dep":"IT",
        "number":"3020",
    },
          "3079":{
        "name":"mohanad ashraf",
        "dep":"IT",
        "number":"3079",
    },
          "3105":{
        "name":"ahmed mohamed",
        "dep":"CS",
        "number":"3105",
    },
              "3162":{
        "name":"abdelgani",
        "dep":"CS",
        "number":"3162",
    },
                "3025":{
        "name":"shrouk adnan",
        "dep":"IT",
        "number":"3025",
    },
                "3034":{
        "name":"abdelrhman essam",
        "dep":"IT",
        "number":"3034",
    },
                "3135":{
        "name":"Rahma",
        "dep":"IT",
        "number":"3135",
    },
                "3080":{
        "name":"momen ahmed",
        "dep":"IT",
        "number":"3080",
    },
        
                "3012":{
        "name":"ahmed mohamed",
        "dep":"IT",
        "number":"3012",
    },
                "3173":{
        "name":"mohamed elsayed",
        "dep":"CS",
        "number":"3173",
    },
                "3130":{
        "name":"khaled ahmed",
        "dep":"",
        "number":"3130",
    },
                "3190":{
        "name":"momen gamal",
        "dep":"CS",
        "number":"3190",
    },
                "3004":{
        "name":"ahmed ashraf",
        "dep":"IT",
        "number":"3004",
    },
                "3142":{
        "name":"Ziad yosry",
        "dep":"",
        "number":"3142",
    },
                "3127":{
        "name":"Habiba adel",
        "dep":"CS",
        "number":"3127",
    },
                "3081":{
        "name":"nancy khaled",
        "dep":"CS",
        "number":"3081",
    },
          "3187":{
        "name":"mostafa mahmoud",
        "dep":"CS",
        "number":"3187",
    },
          "3122":{
        "name":"Beshoy ashraf",
        "dep":"CS",
        "number":"3122",
    },
          "3116":{
        "name":"ashraf essam",
        "dep":"CS",
        "number":"3116",
    },
          "3023":{
        "name":"sarah ahmed",
        "dep":"IT",
        "number":"3023",
    },
          "3001":{
        "name":"Ibrahim Ragab",
        "dep":"IT",
        "number":"3001",
    },
          "3006":{
        "name":"ahmed salama",
        "dep":"IT",
        "number":"3006",
    },
          "3136":{
        "name":"radwa elsaid",
        "dep":"CS",
        "number":"3136",
    },
          "3087":{
        "name":"norhan kamal",
        "dep":"CS",
        "number":"3087",
    },
          "3076":{
        "name":"mostafa elshewy",
        "dep":"CS",
        "number":"3076",
    },
              "3031":{
        "name":"abdelrhman saad",
        "dep":"IT",
        "number":"3031",
    },
      "3170":{
        "name":"ali ali",
        "dep":"CS",
        "number":"3170",
    },

  "3150":{
        "name":"Diaa Hmada",
        "dep":"CS",
        "number":"3150",
    },

  "3128":{
        "name":"Hassan Mohamed",
        "dep":"CS",
        "number":"3128",
    },

  "3153":{
        "name":"abderhman ahmed",
        "dep":"CS",
        "number":"3153",
    },

  "3035":{
        "name":"abdelrhman mohamed",
        "dep":"IT",
        "number":"3035",
    },

  "3195":{
        "name":"Nour Ehab",
        "dep":"CS",
        "number":"3195",
    },

  "3166":{
        "name":"Abdullah mohamed",
        "dep":"CS",
        "number":"3166",
    },

  "3182":{
        "name":"Marwan Ahmed",
        "dep":"CS",
        "number":"3182",
    },

  "3119":{
        "name":"Aya Essam",
        "dep":"CS",
        "number":"3119",
    },

  "4000":{
        "name":"Ahmed Saad",
        "dep":"IT",
        "number":"4000",
    },

  "3009":{
        "name":"Ahmed Abdelhady",
        "dep":"IT",
        "number":"3009",
    },

  "3141":{
        "name":"Ziad Elkhamary",
        "dep":"CS",
        "number":"3141",
    },

  "3192":{
        "name":"Mian Zarif",
        "dep":"CS",
        "number":"3192",
    },

  "3147":{
        "name":"Shahd Hassan",
        "dep":"CS",
        "number":"3147",
    },

  "3188":{
        "name":"Mona Shehata",
        "dep":"CS",
        "number":"3188",
    },

  "3029":{
        "name":"Atef Elsaid",
        "dep":"IT",
        "number":"3029",
    },

  "3037":{
        "name":"Abdelrhman Yasser",
        "dep":"IT",
        "number":"3037",
    },

  "3102":{
        "name":"Ahmed Shieba",
        "dep":"CS",
        "number":"3102",
    },

  "3049":{
        "name":"Fathy saaid",
        "dep":"IT",
        "number":"3049",
    },

  "3075":{
        "name":"Mahmoud Maher",
        "dep":"IT",
        "number":"3075",
    },

  "3148":{
        "name":"Shahd Mohamed",
        "dep":"CS",
        "number":"3148",
    },

  "3124":{
        "name":"Hamed Khaled",
        "dep":"CS",
        "number":"3124",
    },

  "3132":{
        "name":"Khaled Hesham",
        "dep":"CS",
        "number":"3132",
    },

  "3158":{
        "name":"Abdelrhman Mahmoud",
        "dep":"CS",
        "number":"3158",
    },

  "3202":{
        "name":"Yousef Adel",
        "dep":"CS",
        "number":"3202",
    },

  "3108":{
        "name":"Ahmed Mohamed",
        "dep":"CS",
        "number":"3108",
    },

  "3140":{
        "name":"Ziad Ragab",
        "dep":"CS",
        "number":"3140",
    },

  "3191":{
        "name":"Mison Essam",
        "dep":"CS",
        "number":"3191",
    },
      "3002":{
        "name":"Ebrahim Zaid",
        "dep":"IT",
        "number":"3002",
    },
      "3068":{
        "name":"Mohamed Abdelsamad",
        "dep":"IT",
        "number":"3068",
    },
      "3180":{
        "name":"Mohamed Yosry",
        "dep":"CS",
        "number":"3180",
    },
      "3111":{
        "name":"Adham Gamal",
        "dep":"CS",
        "number":"3111",
    },
      "3062":{
        "name":"Mohamed Khaled",
        "dep":"IT",
        "number":"3062",
    },
      "3018":{
        "name":"Eyad Hesham",
        "dep":"IT",
        "number":"3018",
    },
      "3013":{
        "name":"Adham Ashraf",
        "dep":"IT",
        "number":"3013",
    },
    "3204":{
        "name":"Yosef Wael",
        "dep":"CS",
        "number":"3204",
    },
        "3160":{
        "name":"Abdelaaty elfdawy",
        "dep":"CS",
        "number":"3160",
    },



}
for key,value in data.items():
    ref.child(key).set(value)