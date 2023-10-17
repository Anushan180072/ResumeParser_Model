import spacy

nlp = spacy.load("./output_model/model-best")

text = """
B V V M Srinivas Malla
Visakhapatnam, Andhra Pradesh, 530008 | mallsrinivas09@gmail.com | Linkedin
Education

Nxtwave Disruptive Technologies						                          May ’21 - Ongoing
Industry Ready Certification in Full-stack Development 
Kaushik College of Engineering, Visakhapatnam                    	        	                                                  2015
Bachelors in Electronics and Communication Engineering (ECE) [74.67%]
Sri Chaitanya Co-op. Jr College, Visakhapatnam                            	        	                                      2011
Intermediate (Mathematics, Physics, Chemistry) [89.50%]
Kendriya Vidyalaya No. II, Viskahapatnam                            	        	                                                  2009
Secondary School Of Certificate [76.67%]
Skills

Frontend    :  HTML, CSS, Bootstrap, JavaScript, React.js*
Backend     :  Python, Express*, Node.js
Databases   :  SQLite
*courses yet to be completed
Work Experience
Patra Corp - Process Executive -3, Visakhapatnam					     Aug ’16 - Sep ‘21
●	Organize all operations, focusing on quality and consistency 
●	Adjusted client policy plans as requested, calculating and providing new quotes based on coverage   
            details 
●	Analyze documents and requests, and proceed with speed and efficiency
●	Knowledge of Excel, word
●	Obtain necessary client information to establish new policies and update current policies
●	Meets daily productivity and quality targets.
Projects

WeatherApp
Developed weather application using React js with Open weather API get call.
●	Implemented by taking input city from input html element using API get call to display the humidity,  
            temperature, pressure, wind.
●	Each component is designed using react styled components concepts.
●	Search Icon is implemented by material UI icon.
●	Back button element is implemented by material UI button.
Technologies used: HTML, CSS,  JavaScript, React.js, MaterialUI, Axios, Open Weather API, Styled Components, React Hooks - useState                                                    https://weatherapplication1.netlify.app
KeeperApp
Developed persistent notes application with CRUD operations to track list of tasks
●	Implemented by taking input from input html elements and saving as a note , JavaScript event listeners   
            & filtered using Array filter method.
Technologies used: HTML, CSS,  JavaScript, React.js, MaterialUI                        keepernotesapp.netlify.app


Speedometer
●	Developed a responsive website using reactjs it is a speedometer application. Initially the speed was  
            0mph.
●	When Accelerate button is clicked,
●	If the speed is less than 200mph, the speed should be increased by 10mph
●	If the speed is equal to 200mph, the speed should not be increased
●	When Apply Brake button is clicked,
●	If the speed is greater than 0mph, then the speed should be decreased by 10mph
●	If the speed is equal to 0mph, the speed should not be decreased
Technologies used: HTML, CSS, JavaScript, ReactJs	                                      speedometermb.ccbp.tech
Click Counter
Developed a responsive website using reactjs it is counter application when it is on button element.
Technologies used: HTML, CSS, JavaScript, React.js                                                 clickbuttonmb.ccbp.tech
My Projects
Developed a website where people like interviewers can see list of projects that a person implemented
●	Designed a banner section and the project cards using different HTML block, inline elements.
●	Styled the website using CSS3 properties such as background, flex, and CSS box model properties and   
            relative units such as vh, vw, and used absolute units such as px.
Technologies used: HTML, CSS, Bootstrap                                                                 myprojectsmb.ccbp.tech
"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
