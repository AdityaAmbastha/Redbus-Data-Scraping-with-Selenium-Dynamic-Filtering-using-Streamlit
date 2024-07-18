import streamlit as st
import mysql.connector
import pandas as pd
from datetime import time



def fetch_data(query):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="redbus_data_scraping_PROJECT"
    )
    cursor = con.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    # Get column names
    column_names = [column[0] for column in cursor.description]
    con.close()
    return rows,column_names


with st.sidebar:
    state_transport_corp = st.selectbox('Select the State Transport Corporation:',
    ['Kerala (KSRTC)', 'Kadamba (KTCL)', 'Rajasthan (RSRTC)','Himachal Pradesh (HRTC)','Punjab (PEPSU)','Bihar (BSRTC)',
     'South Bengal (SBSTC)','West Bengal','Chandigarh (CTU)','Assam (ASTC)'])
    
    if state_transport_corp == 'Kerala (KSRTC)':
        route = ['Bangalore to Kozhikode', 'Kozhikode to Ernakulam', 'Kozhikode to Bangalore', 
                 'Ernakulam to Kozhikode', 'Kozhikode to Mysore', 'Kozhikode to Thiruvananthapuram', 
                 'Bangalore to Kalpetta (kerala)', 'Mysore to Kozhikode', 'Kalpetta (kerala) to Bangalore', 
                 'Kozhikode to Thrissur', 'Thiruvananthapuram to Kozhikode', 'Bangalore to Kannur', 
                 'Kozhikode to Kottayam', 'Kannur to Bangalore', 'Kottayam to Kozhikode', 
                 'Thrissur to Kozhikode', 'Kozhikode to Kalpetta (kerala)', 'Coimbatore to Ooty', 
                 'Kalpetta (kerala) to Kozhikode']
    elif state_transport_corp == 'Kadamba (KTCL)':
        route = ['Pune to Goa', 'Goa to Pune', 'Mumbai to Goa', 'Goa to Mumbai', 'Pandharpur to Goa', 
                 'Bangalore to Goa', 'Goa to Pandharpur', 'Belagavi to Goa', 'Goa to Bangalore', 
                 'Solapur to Goa', 'Goa to Kolhapur(Maharashtra)', 'Goa to Solapur', 'Goa to Sangola (Solapur)', 
                 'Sangola (Solapur) to Goa', 'Calangute (goa) to Goa Airport', 'Goa to Sangli', 'Calangute (goa) to Mopa Airport', 
                 'Mopa Airport to Calangute (goa)', 'Ponda to Belagavi', 'Goa to Miraj', 'Goa Airport to Calangute (goa)', 
                 'Marcel to Belagavi', 'Shivamogga to Goa', 'Goa to Mopa Airport', 'Goa to Satara', 'Belagavi to Marcel', 
                 'Mopa Airport to Goa', 'Shirdi to Goa', 'Goa to Shivamogga', 'Goa to Shirdi', 'Goa to Goa Airport', 
                 'Margao to Mopa Airport', 'Goa Airport to Goa', 'Mopa Airport to Margao', 'Belagavi to Saquelim', 
                 'Panaji to Mopa Airport', 'Saquelim to Belagavi', 'Calangute (goa) to Goa', 'Calangute (goa) to Panaji', 
                 'Goa Airport to Panaji']
    elif state_transport_corp == 'Rajasthan (RSRTC)':
        route = ['Jodhpur to Ajmer', 'Beawar (Rajasthan) to Jaipur (Rajasthan)', 'Udaipur to Jodhpur', 
                 'Jaipur (Rajasthan) to Jodhpur', 'Sikar to Jaipur (Rajasthan)', 'Kishangarh to Jaipur (Rajasthan)', 
                 'Aligarh (uttar pradesh) to Jaipur (Rajasthan)', 'Jodhpur to Beawar (Rajasthan)', 'Kota(Rajasthan) to Jaipur (Rajasthan)', 
                 'Jaipur (Rajasthan) to Aligarh (uttar pradesh)', 'Jaipur (Rajasthan) to Kota(Rajasthan)', 
                 'Pali (Rajasthan) to Udaipur', 'Udaipur to Pali (Rajasthan)', 'Sikar to Bikaner', 'Jaipur (Rajasthan) to Bharatpur', 
                 'Kishangarh to Jodhpur', 'Jaipur (Rajasthan) to Bhilwara', 'Kota(Rajasthan) to Udaipur', 'Jaipur (Rajasthan) to Pilani', 
                 'Jaipur (Rajasthan) to Mathura', 'Bikaner to Sikar']
    elif state_transport_corp == 'Himachal Pradesh (HRTC)':
        route = ['Delhi to Shimla', 'Shimla to Delhi', 'Manali to Chandigarh', 'Chandigarh to Manali', 
                 'Delhi to Manali', 'Hamirpur (Himachal Pradesh) to Chandigarh', 'Delhi to Hamirpur (Himachal Pradesh)', 
                 'Delhi to Chandigarh', 'Manali to Delhi', 'Hamirpur (Himachal Pradesh) to Delhi', 'Chandigarh to Hamirpur (Himachal Pradesh)', 
                 'Shimla to Manali', 'Delhi to Dharamshala (Himachal Pradesh)', 'Shimla to Chandigarh', 
                 'Chandigarh to Dharamshala (Himachal Pradesh)', 'Delhi to Baddi (Himachal Pradesh)', 
                 'Dharamshala (Himachal Pradesh) to Chandigarh', 'Chamba (Himachal Pradesh) to Chandigarh', 
                 'Delhi to Dalhousie', 'Delhi to Chamba (Himachal Pradesh)', 'Dalhousie to Delhi', 'Solan to Delhi', 
                 'Delhi to Palampur', 'Dharamshala (Himachal Pradesh) to Delhi', 'Delhi to Solan', 'Chandigarh to Reckong Peo (Himachal Pradesh)', 
                 'Manali to Shimla', 'Palampur to Delhi', 'Chandigarh to Kullu', 'Kangra to Chandigarh', 'Kullu to Chandigarh', 
                 'Delhi to Kangra', 'Chamba (Himachal Pradesh) to Delhi', 'Palampur to Chandigarh', 'Chandigarh to Shimla', 
                 'Chandigarh to Kangra', 'Delhi to Nalagarh', 'Baddi (Himachal Pradesh) to Delhi', 'Kangra to Delhi', 
                 'Ghumarwin to Delhi', 'Delhi to Sarkaghat']
    elif state_transport_corp == 'Punjab (PEPSU)':
        route = ['Patiala to Delhi', 'Delhi to Patiala', 'Ludhiana to Delhi', 'Delhi to Ludhiana', 'Phagwara to Delhi', 
                 'Jalandhar to Delhi', 'Delhi to Jalandhar', 'Patiala to Delhi Airport', 'Jalandhar to Delhi Airport', 
                 'Ludhiana to Delhi Airport', 'Phagwara to Delhi Airport', 'Delhi Airport to Ludhiana', 'Delhi to Phagwara', 
                 'Delhi to Amritsar', 'Amritsar to Delhi', 'Delhi Airport to Patiala', 'Amritsar to Delhi Airport', 
                 'Kapurthala to Delhi', 'Delhi Airport to Jalandhar', 'Chandigarh to Bathinda', 'Chandigarh to Faridkot', 
                 'Chandigarh to Patiala']
    elif state_transport_corp == 'Bihar (BSRTC)':
        route = ['Patna (Bihar) to Bettiah', 'Gopalganj (Bihar) to Delhi', 'Patna (Bihar) to Motihari', 
                 'Delhi to Motihari', 'Bettiah to Patna (Bihar)', 'Motihari to Delhi', 'Patna (Bihar) to Balmiki Nagar (bihar)', 
                 'Balmiki Nagar (bihar) to Patna (Bihar)', 'Patna (Bihar) to Kathmandu', 'Patna (Bihar) to Katihar', 
                 'Patna (Bihar) to Purnea', 'Patna (Bihar) to Hazaribagh', 'Ranchi to Patna (Bihar)', 'Hazaribagh to Patna (Bihar)', 
                 'Patna (Bihar) to Raxaul', 'Muzaffarpur (Bihar) to Kathmandu', 'Patna (Bihar) to Ranchi', 'Muzaffarpur (Bihar) to Ranchi', 
                 'Kathmandu to Patna (Bihar)', 'Ranchi to Muzaffarpur (Bihar)', 'Motihari to Lucknow', 'Lucknow to Motihari', 
                 'Motihari to Kathmandu', 'Agra to Motihari', 'Patna (Bihar) to Janakpur (Nepal)', 'Muzaffarpur (Bihar) to Hazaribagh', 
                 'Purnea to Patna (Bihar)', 'Patna (Bihar) to Araria (Bihar)', 'Darbhanga to Patna (Bihar)', 
                 'Patna (Bihar) to Saharsa', 'Motihari to Agra', 'Hajipur (Bihar) to Kathmandu', 
                 'Kathmandu to Motihari', 'Patna (Bihar) to Forbesganj', 'Ranchi to Hajipur (Bihar)', 
                 'Lucknow to Gopalganj (Bihar)']
    elif state_transport_corp == 'South Bengal (SBSTC)':
        route = ['Burdwan to Kolkata', 'Kolkata to Burdwan', 'Durgapur (West Bengal) to Kolkata', 
                 'Kolkata to Haldia', 'Haldia to Kolkata', 'Kolkata to Durgapur (West Bengal)', 
                 'Kolkata to Arambagh (West Bengal)', 'Digha to Kolkata', 'Kolkata to Digha', 
                 'Kolkata to Bankura', 'Asansol (West Bengal) to Kolkata', 'Midnapore to Kolkata', 
                 'Kolkata to Asansol (West Bengal)', 'Kolkata to Siliguri', 'Kolkata to Nimtouri', 
                 'Siliguri to Kolkata', 'Kolkata to Contai (Kanthi)', 'Digha to Durgapur (West Bengal)', 
                 'Kolkata to Midnapore', 'Kolkata to Nandakumar (west bengal)', 'Kolkata to Mecheda (West Bengal)', 
                 'Durgapur (West Bengal) to Digha', 'Kolkata to Kolaghat', 'Jhargram to Kolkata', 'Digha to Barasat (West Bengal)', 
                 'Durgapur (West Bengal) to Siliguri', 'Midnapore to Barasat (West Bengal)', 'Kolkata to Heria', 
                 'Kolkata to Chandipur (West Bengal)', 'Siliguri to Durgapur (West Bengal)', 'Berhampore (West Bengal) to Durgapur (West Bengal)', 
                 'Berhampore (West Bengal) to Suri', 'Barasat (West Bengal) to Digha', 'Kolkata to Futishanko', 
                 'Barasat (West Bengal) to Midnapore', 'Durgapur (West Bengal) to Berhampore (West Bengal)', 
                 'Durgapur (West Bengal) to Malda', 'Digha to Asansol (West Bengal)', 'Kolkata to Ramnagar (West Bengal)', 
                 'Kolkata to Bajkul (West Bengal)', 'Kolkata to Kirnahar (West Bengal)', 'Durgapur (West Bengal) to Bankura', 
                 'Siliguri to Malda', 'Kolkata to Suri', 'Purulia to Durgapur (West Bengal)']
    elif state_transport_corp == 'West Bengal':    
            route = ['Kolkata to Digha', 'Digha to Kolkata', 'Mandarmani to Kolkata', 
                     'Kolkata to Mandarmani', 'Kolkata to Bakkhali']
    elif state_transport_corp == 'Chandigarh (CTU)':        
            route = ['Chandigarh to Delhi', 'Delhi to Chandigarh', 'Yamuna Nagar to Chandigarh', 
                     'Chandigarh to Shimla', 'Chandigarh to Vrindavan', 'Chandigarh to Yamuna Nagar', 
                     'Chandigarh to Sujanpur (himachal pradesh)', 'Ludhiana to Chandigarh', 'Hamirpur (Himachal Pradesh) to Chandigarh', 
                     'Vrindavan to Chandigarh', 'Chandigarh to Hamirpur (Himachal Pradesh)', 'Sujanpur (himachal pradesh) to Chandigarh', 
                     'Shimla to Chandigarh', 'Chandigarh to Ludhiana', 'Chandigarh to Dharamshala (Himachal Pradesh)', 
                     'Chandigarh to Dehradun', 'Chandigarh to Baijnath', 'Pathankot to Chandigarh', 'Chandigarh to Haridwar', 
                     'Chandigarh to Pathankot', 'Talwara to Chandigarh', 'Dehradun to Chandigarh', 'Amritsar to Chandigarh', 
                     'Chandigarh to Rishikesh', 'Chandigarh to Talwara', 'Chandigarh to Dinanagar (punjab)', 'Dinanagar (punjab) to Chandigarh', 
                     'Rishikesh to Chandigarh', 'Chandigarh to Amritsar', 'Chandigarh to Agra', 'Dharamshala (Himachal Pradesh) to Chandigarh', 
                     'Chandigarh to Katra (jammu and kashmir)', 'Hisar (Haryana) to Chandigarh', 'Rohtak to Chandigarh', 
                     'Chandigarh to Una (Himachal Pradesh)', 'Chandigarh to Jammu (j and k)', 'Chandigarh to Rohtak', 
                     'Chandigarh to Manali', 'Chandigarh to Haldwani', 'Jawala Ji to Chandigarh', 'Agra to Chandigarh', 
                     'Jammu (j and k) to Chandigarh', 'Chandigarh to Hisar (Haryana)', 'Chandigarh to Kathgodam', 'Haridwar to Chandigarh', 
                     'Katra (jammu and kashmir) to Chandigarh', 'Baijnath to Chandigarh', 'Narnaul to Chandigarh', 'Chandigarh to Jawala Ji']
    elif state_transport_corp == 'Assam (ASTC)':         
            route = ['Tezpur to Guwahati', 'Guwahati to Tezpur', 'Nagaon (Assam) to Guwahati', 'Guwahati to Nagaon (Assam)', 'Goalpara to Guwahati', 'Jorhat to North Lakhimpur', 'Dhubri to Guwahati', 'Guwahati to Dhubri', 'North Lakhimpur to Sibsagar', 'North Lakhimpur to Jorhat', 'Dhekiajuli to Guwahati', 'Jorhat to Dibrugarh', 'Jorhat to Dhemaji', 'Sibsagar to North Lakhimpur', 'Dhemaji to Jorhat', 'Tezpur to Dibrugarh', 'Haflong to Guwahati', 'North Lakhimpur to Dibrugarh', 'Jorhat to Tinsukia', 'Dibrugarh to Tezpur', 'Guwahati to Biswanath Charali', 'Guwahati to Haflong', 'Dibrugarh to North Lakhimpur', 'Nagaon (Assam) to Haflong', 'Tezpur to Moran', 'Dibrugarh to Jorhat', 'Guwahati to Silchar', 'Bihpuria to Dibrugarh', 'Haflong to Nagaon (Assam)', 'North Lakhimpur to Tezpur', 'Biswanath Charali to Guwahati', 'Biswanath Charali to Dibrugarh', 'Tinsukia to Jorhat', 'Moran to Tezpur', 'Jorhat to Gogamukh', 'Dibrugarh to Biswanath Charali', 'Gohpur to Guwahati', 'Tinsukia to Tezpur', 'North Lakhimpur to Golaghat', 'Golaghat to North Lakhimpur', 'Silchar to Guwahati', 'Bokakhat to Dibrugarh', 'North Lakhimpur to Moran', 'Tezpur to North Lakhimpur', 'Tezpur to Tinsukia', 'Dibrugarh to Bihpuria', 'Dibrugarh to Bokakhat']
            
    bus_route = st.selectbox('Select the route:',route)

    bus_type = st.selectbox('Select the bus type:',['Sleeper','Seater'])

    air_con = st.selectbox('Select A/C or Non A/C:',['A/C', 'Non A/C'])

    ratings = st.selectbox('Select the ratings:',['4 to 5','3 to 4','2 to 3','1 to 2','0 to 1','unrated'])

    starting_time = st.selectbox('Select the starting time:',['00:00 to 06:00','06:00 to 12:00','12:00 to 18:00','18:00 to 24:00'])

    price_option = ['upto ₹200','upto ₹400','upto ₹600','upto ₹800','upto ₹1000', '₹1000+']
    price = st.select_slider('Select the bus fare:',price_option)
    

    click_button = st.button('search')

if bus_type == 'Sleeper' and air_con == 'A/C':
     bustype_query = """bustype LIKE '%Sleeper%'
                    AND (bustype LIKE '%A/C%' OR
                        bustype LIKE 'A/C%')
                    AND (bustype NOT LIKE '%Non%' OR
                        bustype NOT LIKE 'Non%' OR
                        bustype NOT LIKE 'NON%')"""
elif bus_type == 'Seater' and air_con == 'A/C':
     bustype_query = """bustype LIKE '%Seater%'
                    AND (bustype LIKE '%A/C%' OR
                        bustype LIKE 'A/C%')
                    AND bustype LIKE '%MULTI AXLE'
                    And (bustype NOT LIKE '%Non%' OR
                        bustype NOT LIKE 'Non%' OR
                        bustype NOT LIKE 'NON%')"""
elif bus_type == 'Sleeper' and air_con == 'Non A/C':
     bustype_query = """bustype LIKE '%Sleeper%'
                    AND (bustype LIKE '%Non%' OR
                        bustype LIKE 'Non%' OR
                        bustype LIKE 'NON%')"""  
elif bus_type == 'Seater' and air_con == 'Non A/C':
     bustype_query = """bustype LIKE '%Seater%'
                    AND (bustype LIKE '%Non%' OR
                        bustype LIKE 'Non%' OR
                        bustype LIKE 'NON%')"""         

if ratings == '4 to 5':
     rating_query = """star_rating >= 4 AND
                        star_rating <= 5"""
elif ratings == '3 to 4':
     rating_query = """star_rating >= 3 AND
                        star_rating <= 4"""
elif ratings == '2 to 3':
     rating_query = """star_rating >= 2 AND
                        star_rating <= 3"""
elif ratings == '1 to 2':
     rating_query = """star_rating >= 1 AND
                        star_rating <= 2"""
elif ratings == '0 to 1':
     rating_query = """star_rating > 0 AND
                        star_rating <= 1"""
elif ratings == 'unrated':
     rating_query = "star_rating = 0"

if starting_time == '00:00 to 06:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""
elif starting_time == '06:00 to 12:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""
elif starting_time == '12:00 to 18:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""
elif starting_time == '18:00 to 24:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""


if price == 'upto ₹200':
     price_query = "price <= 200"
elif price == 'upto ₹400':
     price_query = "price <= 400"
elif price == 'upto ₹600':
     price_query = "price <= 600"
elif price == 'upto ₹800':
     price_query = "price <= 800"
elif price == 'upto ₹1000':
     price_query = "price <= 1000"
elif price == '₹1000+':
     price_query = "price >= 1000"

st.title(':rainbow[Bus information for the route]')

# query = f"""SELECT * FROM all_bus_data WHERE
#             route_name = '{bus_route}' AND
#             {bustype_query} AND 
#             {rating_query} AND
#             {time_query};"""

query = f"""SELECT * FROM all_bus_data WHERE
            route_name = '{bus_route}' AND 
            {bustype_query} AND
            {rating_query} AND
            {time_query} AND
            {price_query};"""

if click_button:
        # Fetch data from the database
        data, columns = fetch_data(query)
        # Convert to a DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Convert time columns to appropriate format
        # time_columns = ['departing_time', 'reaching_time']  # time column names
        # for col in time_columns:
        #     if col in df.columns:
        #         df[col] = pd.to_datetime(df[col], format='%H:%M').dt.time
        # df['departing_time'] = pd.to_datetime(df['departing_time'], format='%H:%M').dt.time
        # df['reaching_time'] = pd.to_datetime(df['reaching_time'], format='%H:%M').dt.time

        df['departing_time'] = df['departing_time'].apply(lambda x: (pd.Timestamp('1970-01-01') + x).time() if pd.notna(x) else None)
        df['reaching_time'] = df['reaching_time'].apply(lambda x: (pd.Timestamp('1970-01-01') + x).time() if pd.notna(x) else None)
        # Display the data
        st.write(df)