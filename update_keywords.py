import os
import re

keywords_to_add = [
    'Free online internships in Tamil Nadu', 'Free online internships in Kerala', 'Free online internships in Karnataka',
    'Free online internships in Andhra Pradesh', 'Free online internships in Telangana', 'Free online internships in Maharashtra',
    'Free online internships in Gujarat', 'Free online internships in Rajasthan', 'Free online internships in Uttar Pradesh',
    'Free online internships in Madhya Pradesh', 'Free online internships in Bihar', 'Free online internships in West Bengal',
    'Free online internships in Odisha', 'Free online internships in Jharkhand', 'Free online internships in Chhattisgarh',
    'Free online internships in Punjab', 'Free online internships in Haryana', 'Free online internships in Himachal Pradesh',
    'Free online internships in Uttarakhand', 'Free online internships in Goa', 'Free online internships in Assam',
    'Free online internships in Arunachal Pradesh', 'Free online internships in Manipur', 'Free online internships in Meghalaya',
    'Free online internships in Mizoram', 'Free online internships in Nagaland', 'Free online internships in Tripura',
    'Free online internships in Sikkim', 'Free online internships in Delhi', 'Free online internships in Jammu and Kashmir',
    'Free online internships in Ladakh', 'Free online internships in Puducherry', 'Free online internships in Chandigarh',
    'Free online internships in Andaman and Nicobar Islands', 'Free online internships in Dadra and Nagar Haveli and Daman and Diu',
    'Free online internships in Lakshadweep', 'Free online internships in Chennai', 'Free online internships in Tiruvallur',
    'Free online internships in Chengalpattu', 'Free online internships in Kancheepuram', 'Free online internships in Ranipet',
    'Free online internships in Vellore', 'Free online internships in Tirupathur', 'Free online internships in Tiruvannamalai',
    'Free online internships in Viluppuram', 'Free online internships in Kallakurichi', 'Free online internships in Cuddalore',
    'Free online internships in Salem', 'Free online internships in Namakkal', 'Free online internships in Dharmapuri',
    'Free online internships in Krishnagiri', 'Free online internships in Erode', 'Free online internships in Tiruppur',
    'Free online internships in Coimbatore', 'Free online internships in Nilgiris', 'Free online internships in Karur',
    'Free online internships in Dindigul', 'Free online internships in Madurai', 'Free online internships in Theni',
    'Free online internships in Sivaganga', 'Free online internships in Ramanathapuram', 'Free online internships in Virudhunagar',
    'Free online internships in Thoothukudi', 'Free online internships in Tirunelveli', 'Free online internships in Tenkasi',
    'Free online internships in Kanniyakumari', 'Free online internships in Tiruchirappalli', 'Free online internships in Perambalur',
    'Free online internships in Ariyalur', 'Free online internships in Thanjavur', 'Free online internships in Tiruvarur',
    'Free online internships in Nagapattinam', 'Free online internships in Mayiladuthurai', 'Free online internships in Pudukkottai',
    'Free online internships in Bengaluru', 'Free online internships in Mysuru', 'Free online internships in Mangaluru',
    'Free online internships in Hubballi', 'Free online internships in Dharwad', 'Free online internships in Belagavi',
    'Free online internships in Ballari', 'Free online internships in Davanagere', 'Free online internships in Shivamogga',
    'Free online internships in Tumakuru', 'Free online internships in Udupi', 'Free online internships in Kalaburagi',
    'Free online internships in Vijayapura', 'Free online internships in Raichur', 'Free online internships in Hassan',
    'Free online internships in Mandya', 'Free online internships in Chitradurga', 'Free online internships in Kolar',
    'Free online internships in Kodagu', 'Free online internships in Bidar', 'Free online internships in Chikkamagaluru',
    'Free online internships in Bagalkot', 'Free online internships in Gadag', 'Free online internships in Haveri',
    'Free online internships in Koppal', 'Free online internships in Yadgir', 'Free online internships in Visakhapatnam',
    'Free online internships in Vijayawada', 'Free online internships in Guntur', 'Free online internships in Tirupati',
    'Free online internships in Nellore', 'Free online internships in Kurnool', 'Free online internships in Kadapa',
    'Free online internships in Anantapur', 'Free online internships in Chittoor', 'Free online internships in Rajahmundry',
    'Free online internships in Kakinada', 'Free online internships in Eluru', 'Free online internships in Ongole',
    'Free online internships in Srikakulam', 'Free online internships in Vizianagaram', 'Free online internships in Machilipatnam',
    'Free online internships in Bhimavaram', 'Free online internships in Nandyal', 'Free online internships in Anakapalli',
    'Free online internships in Amalapuram', 'Free online internships in Hyderabad', 'Free online internships in Warangal',
    'Free online internships in Nizamabad', 'Free online internships in Karimnagar', 'Free online internships in Khammam',
    'Free online internships in Nalgonda', 'Free online internships in Adilabad', 'Free online internships in Mahbubnagar',
    'Free online internships in Siddipet', 'Free online internships in Suryapet', 'Free online internships in Medak',
    'Free online internships in Sangareddy', 'Free online internships in Jagtial', 'Free online internships in Mancherial',
    'Free online internships in Kamareddy', 'Free online internships in Thiruvananthapuram', 'Free online internships in Kollam',
    'Free online internships in Pathanamthitta', 'Free online internships in Alappuzha', 'Free online internships in Kottayam',
    'Free online internships in Idukki', 'Free online internships in Ernakulam', 'Free online internships in Thrissur',
    'Free online internships in Palakkad', 'Free online internships in Malappuram', 'Free online internships in Kozhikode',
    'Free online internships in Wayanad', 'Free online internships in Kannur', 'Free online internships in Kasaragod',
    'Free online internships in Mumbai', 'Free online internships in Pune', 'Free online internships in Nagpur',
    'Free online internships in Nashik', 'Free online internships in Thane', 'Free online internships in Aurangabad',
    'Free online internships in Kolhapur', 'Free online internships in Solapur', 'Free online internships in Amravati',
    'Free online internships in Satara', 'Free online internships in Sangli', 'Free online internships in Ahmednagar',
    'Free online internships in Jalgaon', 'Free online internships in Nanded', 'Free online internships in Latur',
    'Free online internships in Akola', 'Free online internships in Ratnagiri', 'Free online internships in Chandrapur',
    'Free online internships in Dhule', 'Free online internships in Beed', 'Free online internships for students in Delhi',
    'Free internships with certificate in Delhi', 'Online internships for college students in Delhi', 'Remote internships for students in Delhi',
    'Free online internships in Ahmedabad', 'Free online internships in Jaipur', 'Free online internships in Lucknow',
    'Free online internships in Kanpur', 'Free online internships in Noida', 'Free online internships in Gurugram',
    'Free online internships in Bhopal', 'Free online internships in Indore', 'Free online internships in Patna',
    'Free online internships in Ranchi', 'Free online internships in Bhubaneswar', 'Free online internships in Kolkata',
    'Free online internships in Guwahati', 'Free online internships in Raipur', 'Free online internships in Dehradun',
    'Free online internships in Shimla', 'Free online internships in Jammu', 'Free online internships in Srinagar',
    'Free online internships in Panaji'
]

keywords_str = ", ".join([k.lower() for k in keywords_to_add])

files_to_update = ["index.html", "register.html", "faq.html"]

for f in files_to_update:
    path = os.path.join(r"c:\Users\harih\Downloads\InternCircle-main", f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    match = re.search(r"<meta name=\"keywords\" content=\"([^\"]+)\"", content)
    if match:
        existing_keywords = match.group(1)
        new_keywords = existing_keywords + ", " + keywords_str
        new_content = content[:match.start(1)] + new_keywords + content[match.end(1):]
        with open(path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Updated {f}")
