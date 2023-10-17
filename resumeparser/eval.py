import spacy

nlp = spacy.load("./model/model-best")

text = """
                                                                             RESUME

NARENDRA KOMMINENI
kommineni996@gmail.com	                                                                                                                       Mobile : 8019445089



									

PROFESSIONAL SUMMARY:

•	Having oneyear of experience as a Dot Net Developer in Microsoft .Net Technologies.
•	Having experience in ASP.NET  MVC framework.
•	Extensive experience in developing web applications using C#.net, Asp.net, MVC, Ado.net.
•	Extensive experience in client-side development using   JQuery, JavaScript,Ajax.
•	Experience in programming LINQ queries.
•	Havingexperience in SQL Server to Create Tables, Stored Procedures, Triggers,Functions,Views.
•	Having experience in Bootstrap framework.


TECHNICAL SKILLS:     


Languages	C#.net
Web Technologies	Asp.net, Asp.net MVC, HTML, Ajax, Bootstrap
Client-side Technologies	 Javascript, JQuery 
Database	MS SQL, SQL Server 2014
Tools	Visual Studio 2017,2015
Operatings	Windows Family
Frameworks and Architectures	MS.NET 4.5/4.0



WORK EXPERIENCE:

Working as a Software Developer with National Informatics Center from  Feb ’2021 to Till Now



PROJECT DETAILS:




PROJECT :

Title			:      RythuBandhu.
Client			:      National Informatics Center.	
Duration                           :      Jan’2021 to TillNow  
Project Url                        :      http://rythubandhu.telangana.gov.in


PROJECT DESCRIPTION:

Agriculture Investment Support Scheme” (“Rythu Bandhu”) is proposed to be implemented from the year 2018-19 Kharif season onwards to take care of initial investment needs of every farmer. A budget of Rs.12,000 Crores has been provided for the financial year 2018-19 by Government of Telangana.


ROLES &RESPONSIBILITIES :

•	Requirements gathering and Developing Requirement Specification Document
•	Understanding the Given Requirements and analyzing the code.
•	Transferring the files from the client lo the server location(Web Hosting) by using a tool called FileZilla.
•	Deploying a website using IIS



Environment:  Visual Studio 2015,2017, C#.net, Asp.net, jquery Ajax, JQUERY and SQL Server 2014. 


ACADEMIC PROFILE :	
	B.TECH Electronics and Communications from RVR&JC College of Engineering, Guntur. 2013 to 2016.

	State Board of Technical Education And Training Hyderabad (Diploma) 2010 to 2013.

	Board of Secondary Education from ZPH School 2009 to 2010.


	
 PERSONAL DETAILS :

	Name                     :      Narendra Kommineni
	Father Name        :      Thirupathirao
	Gender                  :      Male
	Date of Birth        :      02-04-1995	
	Address                 :     Janapadu, Piduguralla (Mandal), Guntur(Dist), Andhra Pradesh.
	Nationality            :      Indian.


 DECLARATION:


 I hereby declare that the information given above is true & correct to the best of my knowledge.

	    (Narendra K) 


"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
