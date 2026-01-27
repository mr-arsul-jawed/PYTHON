Name_list=[
  "Aarav","Aisha","Alex","Anaya",
  "Ben","Bella","Bilal","Bhavya",
  "Chris","Chloe","Cyrus","Charu",
  "Daniel","Diya","David","Deepak",
  "Ethan","Emma","Esha","Elina",
  "Farhan","Fatima","Finn","Freya",
  "Gabriel","Grace","Gaurav","Gia",
  "Harry","Hina","Hassan","Hazel",
  "Ibrahim","Isha","Isaac","Ivy",
  "James","Jiya","Jacob","Jasmine",
  "Kabir","Khushi","Kevin","Kiara",
  "Liam","Laila","Laksh","Lily",
  "Mohammad","Meera","Michael","Maya",
  "Noah","Neha","Nikhil","Nora",
  "Omar","Olivia","Om","Oishi",
  "Paul","Priya","Peter","Pihu",
  "Qasim","Quinn","Qadir","Queenie",
  "Rahul","Riya","Ryan","Rose",
  "Sam","Sara","Siddharth","Sofia",
  "Thomas","Tanvi","Taha","Tina",
  "Umar","Usha","Uday","Uma",
  "Vikram","Vaishali","Victor","Violet",
  "William","Wafa","Wendy","Wasim",
  "Xavier","Xenia",
  "Yusuf","Yash","Yara","Yuvika",
  "Zain","Zara","Zoe","Zubair"
]

A_type_names=[]
Another_name=[]

def filter_name(arr):
    for name in arr:
        if name.startswith('A'):
            A_type_names.append(name)
        else:
            Another_name.append(name)
    return A_type_names



result=filter_name(Name_list)
print(result)