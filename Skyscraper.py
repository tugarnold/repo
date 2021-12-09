"""
Name: Tug Arnold
CS230: Section 005
Data: Skyscrapers
URL: Link to your web application online

Description:

This program reads in data from a csv file and presents it in three different formats.
First, it presents a map-based format where the user can see skyscrapers of a certain size or in a certain country.
Secondly, there is a function that compares two or more buildings and the number of floors they have.
Lastly, there is a histogram section that contains a multitude of histograms pertaining to the dataset.
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns # used new package seaborn for the histograms
import folium # used folium for the first time as well as streamlit_folium to upload it statically
from streamlit_folium import folium_static

columns = ['RANK', 'NAME', 'CITY', 'Full Address', 'Country', 'Latitude', 'Longitude', 'COMPLETION', 'Height', 'Meters', 'Feet', 'FLOORS', 'MATERIAL', 'FUNCTION', 'Link']
buildings = []
addresses = []
global data
data = pd.read_csv("Skyscrapers2021.csv")
building_functions = data["FUNCTION"].drop_duplicates()
heights = data["Meters"]
countries = data["Country"].drop_duplicates() # added in a country column to csv file because it should have been there in the first place
global china_list
china_list = [{"NAME": "Shanghai Tower", "Link": "https://www.skyscrapercenter.com/building/shanghai-tower/56", "Latitude": 31.2335, "Longitude": 121.5056},
                 {"NAME": "Ping An Finance Center", "Link": "https://www.skyscrapercenter.com/building/ping-an-finance-center/54", "Latitude": 22.5331, "Longitude": 114.0559},
                 {"NAME": "Guangzhou CTF Finance Centre", "Link": "https://www.skyscrapercenter.com/building/guangzhou-ctf-finance-centre/176", "Latitude": 23.1176, "Longitude": 113.3259},
                 {"NAME": "Tianjin CTF Finance Centre", "Link": "https://www.skyscrapercenter.com/building/tianjin-ctf-finance-centre/310", "Latitude": 39.021667, "Longitude": 117.698056},
                 {"NAME": "CITIC Tower", "Link": "https://www.skyscrapercenter.com/building/citic-tower/11116", "Latitude": 39.930818, "Longitude": 116.4359296},
                 {"NAME": "Shanghai World Financial Center", "Link": "https://www.skyscrapercenter.com/building/shanghai-world-financial-center/131", "Latitude": 31.2342797, "Longitude": 121.5079157},
                 {"NAME": "International Commerce Centre", "Link": "https://www.skyscrapercenter.com/building/international-commerce-centre/137", "Latitude": 22.3034032, "Longitude": 114.1601907},
                 {"NAME": "Changsha IFS Tower T1", "Link": "https://www.skyscrapercenter.com/building/changsha-ifs-tower-t1/13144", "Latitude": 28.191892, "Longitude": 112.97693},
                 {"NAME": "Suzhou IFS", "Link": "https://www.skyscrapercenter.com/building/suzhou-ifs/196", "Latitude": 31.3222031, "Longitude": 120.7171222},
                 {"NAME": "Zifeng Tower", "Link": "https://www.skyscrapercenter.com/building/zifeng-tower/165", "Latitude": 32.062472, "Longitude": 118.778056},
                 {"NAME": "Wuhan Center Tower", "Link": "https://www.skyscrapercenter.com/building/wuhan-center-tower/8823", "Latitude": 30.580437, "Longitude": 114.268548},
                 {"NAME": "KK100", "Link": "https://www.skyscrapercenter.com/building/kk100/173", "Latitude": 22.542218, "Longitude": 114.106514},
                 {"NAME": "Guangzhou International Finance Center", "Link": "https://www.skyscrapercenter.com/building/guangzhou-international-finance-center/174", "Latitude": 23.1177169, "Longitude": 113.3232779},
                 {"NAME": "Jin Mao Tower", "Link": "https://www.skyscrapercenter.com/building/jin-mao-tower/189", "Latitude": 31.2352515, "Longitude": 121.5057491},
                 {"NAME": "Two International Finance Centre", "Link": "https://www.skyscrapercenter.com/building/two-international-finance-centre/205", "Latitude": 22.28588, "Longitude": 114.158131},
                 {"NAME": "Guangxi China Resources Tower", "Link": "https://www.skyscrapercenter.com/building/guangxi-china-resources-tower/33180", "Latitude": 22.817002, "Longitude": 108.366543},
                 {"NAME": "Guiyang International Financial Center T1", "Link": "https://www.skyscrapercenter.com/building/guiyang-international-financial-center-t1/33699", "Latitude": 26.647794, "Longitude": 106.647407},
                 {"NAME": "China Resources Tower", "Link": "https://www.skyscrapercenter.com/building/china-resources-tower/14589", "Latitude": 22.5126787, "Longitude": 113.9457475},
                 {"NAME": "CITIC Plaza", "Link": "https://www.skyscrapercenter.com/building/citic-plaza/242", "Latitude": 23.1423581, "Longitude": 113.3247658},
                 {"NAME": "Shum Yip Upperhills Tower 1", "Link": "https://www.skyscrapercenter.com/building/shum-yip-upperhills-tower-1/16001", "Latitude": 22.6433733, "Longitude": 114.0232686},
                 {"NAME": "Shun Hing Square", "Link": "https://www.skyscrapercenter.com/building/shun-hing-square/258", "Latitude": 22.545278, "Longitude": 114.105833},
                 {"NAME": "Eton Place Dalian Tower 1", "Link": "https://www.skyscrapercenter.com/building/eton-place-dalian-tower-1/249", "Latitude": 38.9165077, "Longitude": 121.6307827},
                 {"NAME": "Nanning Logan Century 1", "Link": "https://www.skyscrapercenter.com/building/nanning-logan-century-1/10698", "Latitude": 22.817002, "Longitude": 108.366543},
                 {"NAME": "Central Plaza", "Link": "https://www.skyscrapercenter.com/building/central-plaza/277", "Latitude": 22.2799097, "Longitude": 114.1737282},
                 {"NAME": "Dalian International Trade Center", "Link": "https://www.skyscrapercenter.com/building/dalian-international-trade-center/8980", "Latitude": 38.920574, "Longitude": 121.637787},
                 {"NAME": "Golden Eagle Tiandi Tower A", "Link": "https://www.skyscrapercenter.com/building/golden-eagle-tiandi-tower-a/11463", "Latitude": 35, "Longitude": 107},
                 {"NAME": "Bank of China Tower", "Link": "https://www.skyscrapercenter.com/building/bank-of-china-tower/287", "Latitude": 22.279304, "Longitude": 114.1614931},
                 {"NAME": "Hanking Center", "Link": "https://www.skyscrapercenter.com/building/hanking-center/15741", "Latitude": 22.543096, "Longitude": 114.057865},
                 {"NAME": "Raffles City Chongqing T3N", "Link": "https://www.skyscrapercenter.com/building/raffles-city-chongqing-t3n/13610", "Latitude": 29.563428, "Longitude": 106.58851},
                 {"NAME": "Raffles City Chongqing T4N", "Link": "https://www.skyscrapercenter.com/building/raffles-city-chongqing-t4n/13611", "Latitude": 29.563428, "Longitude": 106.58851},
                 {"NAME": "Forum 66 Tower 1", "Link": "https://www.skyscrapercenter.com/building/forum-66-tower-1/414", "Latitude": 41.804386, "Longitude": 123.433881},
                 {"NAME": "The Pinnacle", "Link": "https://www.skyscrapercenter.com/building/the-pinnacle/306", "Latitude": 23.1250438, "Longitude": 102.832891},
                 {"NAME": "Spring City 66", "Link": "https://www.skyscrapercenter.com/building/spring-city-66/14797", "Latitude": 24.880095, "Longitude": 120.300315},
                 {"NAME": "Shimao Hunan Center", "Link": "https://www.skyscrapercenter.com/building/shimao-hunan-center/15373", "Latitude": 28.2274307, "Longitude": 112.9386753},
                 {"NAME": "The Center", "Link": "https://www.skyscrapercenter.com/building/the-center/343", "Latitude": 22.2846202, "Longitude": 114.1547347},
                 {"NAME": "One Shenzhen Bay Tower 7", "Link": "https://www.skyscrapercenter.com/building/one-shenzhen-bay-tower-7/13245", "Latitude": 25.1854, "Longitude": 114.057865},
                 {"NAME": "Wuxi International Finance Square", "Link": "https://www.skyscrapercenter.com/building/wuxi-international-finance-square/356", "Latitude": 31.491169, "Longitude": 120.31191},
                 {"NAME": "Heartland 66 Office Tower", "Link": "https://www.skyscrapercenter.com/building/heartland-66-office-tower/16900", "Latitude": 30.592849, "Longitude": 114.305539},
                 {"NAME": "Chongqing World Financial Center", "Link": "https://www.skyscrapercenter.com/building/chongqing-world-financial-center/376", "Latitude": 29.559143, "Longitude": 106.577798},
                 {"NAME": "Suning Plaza Tower 1", "Link": "https://www.skyscrapercenter.com/building/suning-plaza-tower-1/11169", "Latitude": 32.187849, "Longitude": 119.425836},
                 {"NAME": "Tianjin Modern City Office Tower", "Link": "https://www.skyscrapercenter.com/building/tianjin-modern-city-office-tower/9692", "Latitude": 39.119243, "Longitude": 117.197308},
                 {"NAME": "Hengqin International Finance Center", "Link": "https://www.skyscrapercenter.com/building/hengqin-international-finance-center/17752", "Latitude": 22.1274462, "Longitude": 113.5293933},
                 {"NAME": "Tianjin World Financial Center", "Link": "https://www.skyscrapercenter.com/building/tianjin-world-financial-center/360", "Latitude": 39.1297658, "Longitude": 117.2030415},
                 {"NAME": "Twin Towers Guiyang, East Tower", "Link": "https://www.skyscrapercenter.com/building/twin-towers-guiyang-east-tower/15030", "Latitude": 26.647661, "Longitude": 26.647661},
                 {"NAME": "Twin Towers Guiyang, West Tower", "Link": "https://www.skyscrapercenter.com/building/twin-towers-guiyang-west-tower/15031", "Latitude": 26.647661, "Longitude": 26.647661},
                 {"NAME": "Shimao International Plaza", "Link": "https://www.skyscrapercenter.com/building/shimao-international-plaza/370", "Latitude": 31.2343464, "Longitude": 121.4760796},
                 {"NAME": "Jinan Center Financial City A5-3", "Link": "https://www.skyscrapercenter.com/building/jinan-center-financial-city-a5-3/16323", "Latitude": 36.6512, "Longitude": 117.12009},
                 {"NAME": "Minsheng Bank Building", "Link": "https://www.skyscrapercenter.com/building/minsheng-bank-building/374", "Latitude": 30.594394, "Longitude": 114.272755},
                 {"NAME": "China World Tower", "Link": "https://www.skyscrapercenter.com/building/china-world-tower/379", "Latitude": 39.909511, "Longitude": 116.458172},
                 {"NAME": "Yuexiu Fortune Center Tower 1", "Link": "https://www.skyscrapercenter.com/building/yuexiu-fortune-center-tower-1/14600", "Latitude": 30.569091, "Longitude": 114.250473}]
global kuwait_list
kuwait_list = [{"NAME": "Al Hamra Tower", "Link": "https://www.skyscrapercenter.com/building/al-hamra-tower/208", "Latitude": 29.3790539, "Longitude": 47.9932879}]
global malaysia_list
malaysia_list = [{"NAME": "Petronas Twin Tower 1", "Link": "https://www.skyscrapercenter.com/building/petronas-twin-tower-1/149", "Latitude": 3.1579603, "Longitude": 101.7117668},
                 {"NAME": "Petronas Twin Tower 2", "Link": "https://www.skyscrapercenter.com/building/petronas-twin-tower-2/150", "Latitude": 3.157960, "Longitude": 101.7117668},
                 {"NAME": "The Exchange 106", "Link": "https://www.skyscrapercenter.com/building/the-exchange-106/24971", "Latitude": 3.1418361, "Longitude": 101.7186957},
                 {"NAME": "Four Seasons Place", "Link": "https://www.skyscrapercenter.com/building/four-seasons-place/5211", "Latitude": 3.1581663, "Longitude": 101.7135536}]
global russia_list
russia_list = [{"NAME": "Lakhta Center", "Link": "https://www.skyscrapercenter.com/building/lakhta-center/12575", "Latitude": 59.9871, "Longitude": 30.1777},
                 {"NAME": "Federation Tower", "Link": "https://www.skyscrapercenter.com/building/federation-tower/118", "Latitude": 55.7464, "Longitude": 37.5365},
                 {"NAME": "OKO - Residential Tower", "Link": "https://www.skyscrapercenter.com/building/oko-residential-tower/363", "Latitude": 55.7499, "Longitude": 37.5344},
                 {"NAME": "NEVA TOWERS 2", "Link": "https://www.skyscrapercenter.com/building/neva-towers-2/233", "Latitude": 55.7514, "Longitude": 37.5357},
                 {"NAME": "Mercury City Tower", "Link": "https://www.skyscrapercenter.com/building/mercury-city-tower/265", "Latitude": 55.7506, "Longitude": 37.5396}]
global sa_list
sa_list = [{"NAME": "Makkah Royal Clock Tower", "Link": "https://www.skyscrapercenter.com/building/makkah-royal-clock-tower/84", "Latitude": 21.4187, "Longitude": 39.8253}]
global sk_list
sk_list = [{"NAME": "Lotte World Tower", "Link": "https://www.skyscrapercenter.com/building/lotte-world-tower/88", "Latitude": 37.5125, "Longitude": 127.1024},
            {"NAME": "LCT The Sharp Landmark Tower", "Link": "https://www.skyscrapercenter.com/building/lct-the-sharp-landmark-tower/108", "Latitude": 35.1611, "Longitude": 129.1684},
            {"NAME": "LCT The Sharp Residential Tower A", "Link": "https://www.skyscrapercenter.com/building/lct-the-sharp-residential-tower-a/235", "Latitude": 35.1611, "Longitude": 129.1684},
            {"NAME": "LCT The Sharp Residential Tower A", "Link": "https://www.skyscrapercenter.com/building/lct-the-sharp-residential-tower-b/12160", "Latitude": 35.1611, "Longitude": 129.1684}]
global taiwan_list
taiwan_list = [{"NAME": "TAIPEI 101", "Link": "https://www.skyscrapercenter.com/building/taipei-101/117", "Latitude": 25.0337, "Longitude": 121.5649},
                 {"NAME": "85 Sky Tower", "Link": "https://www.skyscrapercenter.com/building/85-sky-tower/338", "Latitude": 22.6115, "Longitude": 120.3003}]
global uae_list
uae_list = [{"NAME": "Burj Khalifa", "Link": "https://www.skyscrapercenter.com/building/burj-khalifa/3", "Latitude": 25.1972, "Longitude": 55.2744},
                 {"NAME": "Marina 101", "Link": "https://www.skyscrapercenter.com/building/marina-101/207", "Latitude": 25.0889, "Longitude": 55.1486},
                 {"NAME": "Princess Tower", "Link": "https://www.skyscrapercenter.com/building/princess-tower/206", "Latitude": 25.0888, "Longitude": 55.1469},
                 {"NAME": "23 Marina", "Link": "https://www.skyscrapercenter.com/building/23-marina/247", "Latitude": 25.0897, "Longitude": 55.1506},
                 {"NAME": "Burj Mohammed Bin Rashid", "Link": "https://www.skyscrapercenter.com/building/burj-mohammed-bin-rashid/259", "Latitude": 24.2868, "Longitude": 54.3578},
                 {"NAME": "Elite Residence", "Link": "https://www.skyscrapercenter.com/building/elite-residence/263", "Latitude": 25.0896, "Longitude": 55.1478},
                 {"NAME": "The Address Boulevard", "Link": "https://www.skyscrapercenter.com/building/the-address-boulevard/14606", "Latitude": 25.2003, "Longitude": 55.276},
                 {"NAME": "Almas Tower", "Link": "https://www.skyscrapercenter.com/building/almas-tower/298", "Latitude": 25.069, "Longitude": 55.1412},
                 {"NAME": "Gevora Hotel", "Link": "https://www.skyscrapercenter.com/building/gevora-hotel/348", "Latitude": 25.2125, "Longitude": 55.277},
                 {"NAME": "JW Marriott Marquis Hotel Dubai Tower 1", "Link": "https://www.skyscrapercenter.com/building/jw-marriott-marquis-hotel-dubai-tower-1/237", "Latitude": 25.1854, "Longitude": 55.2581},
                 {"NAME": "JW Marriott Marquis Hotel Dubai Tower 2", "Link": "https://www.skyscrapercenter.com/building/jw-marriott-marquis-hotel-dubai-tower-2/238", "Latitude": 25.1854, "Longitude": 55.2581},
                 {"NAME": "Emirates Tower One", "Link": "https://www.skyscrapercenter.com/building/emirates-tower-one/311", "Latitude": 25.2176, "Longitude": 55.2828},
                 {"NAME": "The Torch", "Link": "https://www.skyscrapercenter.com/building/the-torch/344", "Latitude": 25.0879, "Longitude": 55.1475},
                 {"NAME": "ADNOC Headquarters", "Link": "https://www.skyscrapercenter.com/building/adnoc-headquarters/8763", "Latitude": 24.462, "Longitude": 54.3242},
                 {"NAME": "SLS Dubai", "Link": "https://www.skyscrapercenter.com/building/sls-dubai/26014", "Latitude": 25.1849, "Longitude": 55.2923},
                 {"NAME": "DAMAC Heights", "Link": "https://www.skyscrapercenter.com/building/damac-heights/185", "Latitude": 25.0873, "Longitude": 55.1456},
                 {"NAME": "Rose Rayhaan by Rotana", "Link": "https://www.skyscrapercenter.com/building/rose-rayhaan-by-rotana/369", "Latitude": 25.2118, "Longitude": 55.2766},
                 {"NAME": "The Address Residence - Fountain Views III", "Link": "https://www.skyscrapercenter.com/building/the-address-residence-fountain-views-iii/16604", "Latitude": 25.1945, "Longitude": 55.282}]
global usa_list
usa_list = [{"NAME": "One World Trade Center", "Link": "https://www.skyscrapercenter.com/building/one-world-trade-center/98", "Latitude": 40.7127, "Longitude": -74.0134},
                 {"NAME": "Central Park Tower", "Link": "https://www.skyscrapercenter.com/building/central-park-tower/14269", "Latitude": 40.7661, "Longitude": -73.9809},
                 {"NAME": "Willis Tower", "Link": "https://www.skyscrapercenter.com/building/willis-tower/169", "Latitude": 41.8789, "Longitude": -87.6359},
                 {"NAME": "One Vanderbilt", "Link": "https://www.skyscrapercenter.com/building/one-vanderbilt/15833", "Latitude": 40.753, "Longitude": -73.9785},
                 {"NAME": "432 Park Avenue", "Link": "https://www.skyscrapercenter.com/building/432-park-avenue/13227", "Latitude": 40.7616, "Longitude": -73.9718},
                 {"NAME": "Trump International Hotel & Tower", "Link": "https://www.skyscrapercenter.com/building/trump-international-hotel-tower/203", "Latitude": 41.8889, "Longitude": -87.6264},
                 {"NAME": "30 Hudson Yards", "Link": "https://www.skyscrapercenter.com/building/30-hudson-yards/13325", "Latitude": 40.7536, "Longitude": -74.0032},
                 {"NAME": "Empire State Building", "Link": "https://www.skyscrapercenter.com/building/empire-state-building/261", "Latitude": 40.7484, "Longitude": -73.9857},
                 {"NAME": "Bank of America Tower", "Link": "https://www.skyscrapercenter.com/building/bank-of-america-tower/291", "Latitude": 40.7556, "Longitude": -73.9849},
                 {"NAME": "St. Regis Chicago", "Link": "https://www.skyscrapercenter.com/building/st-regis-chicago/17137", "Latitude": 41.8874, "Longitude": -87.6175},
                 {"NAME": "Aon Center", "Link": "https://www.skyscrapercenter.com/building/aon-center/339", "Latitude": 41.8853, "Longitude": -87.6215},
                 {"NAME": "875 North Michigan Avenue", "Link": "https://www.skyscrapercenter.com/building/875-north-michigan-avenue/345", "Latitude": 41.8989, "Longitude": -87.6232},
                 {"NAME": "Comcast Technology Center", "Link": "thttps://www.skyscrapercenter.com/building/comcast-technology-center/16192", "Latitude": 39.955, "Longitude": -75.1706},
                 {"NAME": "Wilshire Grand Center", "Link": "https://www.skyscrapercenter.com/building/wilshire-grand-center/9686", "Latitude": 34.05, "Longitude": -118.2612}]
global vietnam_list
vietnam_list = [{"NAME": "Vincom Landmark 81", "Link": "https://www.skyscrapercenter.com/building/vincom-landmark-81/18192", "Latitude": 10.7946, "Longitude": 106.7222}]


def splash_page():
    st.title("Welcome to the Skyscraper Scene!", )
    activity = st.radio("How would you like to learn about skyscrapers?", ("Home", "Search skyscrapers by country", "Compare skyscraper heights", "Find skyscrapers according to frequency"))
    if activity == "Search skyscrapers by country":
        where_art_thou_skyscrapers()
    elif activity == "Home":
        print()
    elif activity == "Compare skyscraper heights":
        compare()
    elif activity == "Find skyscrapers according to frequency":
        histogram()


def where_art_thou_skyscrapers():
    st.sidebar.header("Options")
    global data
    country_select = st.sidebar.selectbox("Please select a country:", sorted(countries))
    number = st.sidebar.slider("Building Height (In Meters)", 0, 1000)
    if country_select == "China":
        china_map()
        if number == 0:
            data.loc[data["Country"] == "China", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "China", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "Kuwait":
        kuwait_map()
        if number == 0:
            data.loc[data["Country"] == "Kuwait", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "Kuwait", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "Malaysia":
        malaysia_map()
        if number == 0:
            data.loc[data["Country"] == "Malaysia", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "Malaysia", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "Russia":
        russia_map()
        if number == 0:
            data.loc[data["Country"] == "Russia", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "Russia", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "Saudi Arabia":
        saudiarabia_map()
        if number == 0:
            data.loc[data["Country"] == "Saudi Arabia", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "Saudi Arabia", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "South Korea":
        southkorea_map()
        if number == 0:
            data.loc[data["Country"] == "South Korea", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "South Korea", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "Taiwan":
        taiwan_map()
        if number == 0:
            data.loc[data["Country"] == "Taiwan", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "Taiwan", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "United Arab Emirates":
        uae_map()
        if number == 0:
            data.loc[data["Country"] == "United Arab Emirates", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "United Arab Emirates", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "United States of America":
        usa_map()
        if number == 0:
            data.loc[data["Country"] == "United States of America", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "United States of America", ["NAME", "Latitude", "Longitude", "Meters"]]
    elif country_select == "Vietnam":
        vietnam_map()
        if number == 0:
            data.loc[data["Country"] == "Vietnam", ["NAME", "Latitude", "Longitude", "Meters"]]
        else:
            data["Meters"] = data["Meters"].str.strip(" m")
            data["Meters"] = data["Meters"].astype(float)
            data = data[data["Meters"] < number]
            data.loc[data["Country"] == "Vietnam", ["NAME", "Latitude", "Longitude", "Meters"]]


def compare():
    hello = st.sidebar.title("Options")
    country_select = st.sidebar.selectbox("Please select the skyscrapers you want to compare \n\n Country", sorted(countries))
    selected_buildings = []
    floors = []
    if country_select == "China":
        for row in data.itertuples(): # learned a lot with itertuples in this project and how valuable they are for data organization
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        ax.set_title("Comparing Skyscraper Heights", fontsize=17)
        ax.set_xlabel("Number of Floors", fontsize=12)
        ax.set_ylabel("Skyscraper Name", fontsize=12)
        st.pyplot(fig)
    elif country_select == "Kuwait":
        for row in data.itertuples():
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        st.pyplot(fig)
    elif country_select == "Russia":
        for row in data.itertuples():
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        st.pyplot(fig)
    elif country_select == "South Korea":
        for row in data.itertuples():
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        st.pyplot(fig)
    elif country_select == "United Arab Emirates":
        for row in data.itertuples():
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        st.pyplot(fig)
    elif country_select == "United States of America":
        for row in data.itertuples():
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        st.pyplot(fig)
    elif country_select == "Vietnam":
        for row in data.itertuples():
            if row.Country == country_select:
                selected_buildings.append(row.NAME)
        building_choice = st.sidebar.multiselect("Building", selected_buildings)
        for b in building_choice:
            for row in data.itertuples():
                if row.NAME == b:
                    floors.append(row.FLOORS)

        colors = {"red": "r", "green": "g", "yellow": "y", "blue": "b"}
        colours = []
        color_names = list(colors.keys())

        for c in building_choice:
            selected_color = st.sidebar.radio(f"{c} Color", color_names)
            colours.append(selected_color)

        fig, ax = plt.subplots()
        ax.barh(building_choice, floors, color=colours)
        ax.invert_yaxis()
        st.pyplot(fig)


def histogram(): # here I used the extra seaborn package
    hello = st.sidebar.title("Sidebar")
    hello1 = st.sidebar.write("The three graphs to the right allow you to take a closer look at the skyscraper data presented.")
    hello2 = st.sidebar.write("Floors by Frequency shows which size skyscrapers are the most popular.")
    hello3 = st.sidebar.write("Material by Frequency displays which building materials are most commmon.")
    hello4 = st.sidebar.write("Finally, Country by Frequency shows which countries have the most skyscrapers.")
    graph = sns.histplot(data['FLOORS'], kde=False, color='deepskyblue', bins=20)
    plt.title("Floors by Frequency", fontsize=17)
    plt.xlabel("Floors", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    graph2 = sns.histplot(data["MATERIAL"], kde=False, color = 'magenta', bins=20)
    plt.title("Material by Frequency", fontsize=17)
    plt.xlabel("Material", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    st.pyplot()
    graph3 = sns.histplot(y=data["Country"], kde=False, color='chartreuse')
    plt.title("Country by Frequency", fontsize=17)
    plt.xlabel("Count", fontsize=12)
    plt.ylabel("Country", fontsize=12)
    st.pyplot()


def china_map():
    def showfunc(places):
        center = [35.35, 118]
        map = folium.Map(location=center, zoom_start=4)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)
    # referencing the list of dictionaries made above that contain Chhinese skyscrapers
    def main():
        global china_list
        showfunc(china_list)
    main()


def kuwait_map():
    def showfunc(places):
        center = [29.3117, 47.4818]
        map = folium.Map(location=center, zoom_start=9)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global kuwait_list
        showfunc(kuwait_list)
    main()


def malaysia_map():
    def showfunc(places):
        center = [3.139, 101.6869]
        map = folium.Map(location=center, zoom_start=12)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global malaysia_list
        showfunc(malaysia_list)
    main()


def russia_map():
    def showfunc(places):
        center = [55.7558, 37.6173]
        map = folium.Map(location=center, zoom_start=5)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global russia_list
        showfunc(russia_list)
    main()


def saudiarabia_map():
    def showfunc(places):
        center = [21.3891, 39.8579]
        map = folium.Map(location=center, zoom_start=10)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global sa_list
        showfunc(sa_list)
    main()


def southkorea_map():
    def showfunc(places):
        center = [35.9078, 127.7669]
        map = folium.Map(location=center, zoom_start=7)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global sk_list
        showfunc(sk_list)
    main()


def taiwan_map():
    def showfunc(places):
        center = [23.6978, 120.9605]
        map = folium.Map(location=center, zoom_start=7)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global taiwan_list
        showfunc(taiwan_list)
    main()


def uae_map():
    def showfunc(places):
        center = [24.8, 55]
        map = folium.Map(location=center, zoom_start=9)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global uae_list
        showfunc(uae_list)
    main()


def usa_map():
    def showfunc(places):
        center = [39, -95]
        map = folium.Map(location=center, zoom_start=4)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global usa_list
        showfunc(usa_list)
    main()


def vietnam_map():
    def showfunc(places):
        center = [10.8, 106.75]
        map = folium.Map(location=center, zoom_start=12)
        for place in places:
            lat = place.get("Latitude")
            lon = place.get("Longitude")
            icon = folium.Icon(icon='building', prefix='fa', color='blue')
            folium.Marker(location=[lat, lon],
                          popup= '<a href=\"' + place.get("Link") + '\">' + place.get("Link") + '</a>',
                          tooltip=place.get("NAME"),
                          icon=icon).add_to(map)

        folium_static(map)

    def main():
        global vietnam_list
        showfunc(vietnam_list)
    main()


splash_page()
