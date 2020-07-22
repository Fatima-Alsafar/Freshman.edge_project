from http.server import BaseHTTPRequestHandler, HTTPServer

class OnlinePharmacy(BaseHTTPRequestHandler):


    def make_header(self):
        return( "<html>"
                "<head>"
                "<title>F~OnlinePharmacy</title>"
                "</head>"
                "</body>")

    def make_footer(self):
        return( "</body>"
                "</html>")
# style - www.w3schools.com
    def make_home(self):
        return( "<h2 style = 'color:#9999ff;'>Welcome to F~Online Pharmacy</h2>"
                "<p>This is a website designed to be user friendly as it sets clear directions and simple instructions.</p>"
                "<h3 style = 'color:#ff9999;'>Instructions</h3>"
                "<p>Below is a list of common illness that we prescribe medication to. How this website works: from the list below, choose the one that is relevant to your illness. Next: go ahead to the search bar and you shall see localhost:9011 - all what you need to do is to add a / and type the word that corresponds to the option you chose and press enter.</p> "
                "<h3 style = 'color:#ff9999;'>List:</h3>"
                "<p>allergies - asthma </p>"
                "<p>coldandflu - coughandphlegm</p>"
                "<p>dryeyes</p>"
                "<p>earinfection</p>"
                "<p>headache - heartburn - highfever</p>"
                "<p>jointsprain</p>"
                "<p>minormuscleorjointsprain</p>"
                "<p>pinkeye - preganancyvitaminB</p>"
                "<p>runnynose</p>"
                "<p>teething - toothache</p>")
# definition of allergy - www.aaaai.org
# zyrtec - www.zyrtec.com
# fun facts - www.sciencebob.com
    def make_allergies(self):
        return( "<h2 style = 'color:#9999ff;'>Allergies</h2>"
                "<p>An allergy is a chronic condition involving an abnormal reaction to an ordinarily harmless substance called an allergen. Allergens can include aeroallergens such as dust mite, mold, and tree weed and grass pollen, as well as food allergens such as milk, egg, soy, wheat, nut or fish proteins.</p>"
                "<h3 style = 'color:#ff9999;'>ZYRTEC</h3>"
                "<p>Zyrtec can be used for temporarily relief of the following common allergy symptoms: Runny nose. Sneezing. Itchy, watery eyes.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>2 - 6y rs: drink 2.5ml a day.</p>"
                "<p>7 - 64 yrs: drink around 5-10ml a day depending on severity.</p>"
                "<p>65 + yrs: drink 5ml a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Only 2 % of the entire population have green eyes.</p>")
# definition of asthma - www.mayoclinic.org
# ventolin - www.rxlist.com
    def make_asthma(self):
        return( "<h2 style = 'color:#9999ff;'>Asthma</h2>"
                "<p>Asthma is a condition in which your airways narrow and swell and may produce extra mucus. This can make breathing difficult and trigger coughing, a whistling sound (wheezing) when you breathe out and shortness of breath. For some people, asthma is a minor nuisance.</p>"
                "<h3 style = 'color:#ff9999;'>VENTOLIN</h3>"
                "<p>Albuterol (also known as salbutamol) is used to prevent and treat wheezing and shortness of breath caused by breathing problems (such as asthma, chronic obstructive pulmonary disease). It is also used to prevent asthma brought on by exercise. It is a quick-relief drug.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>1 + yrs: 1-2 inhilations whenever needed</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Your eyelashes last about 150 days.</p>")
# definition of cold&flu - www.cdc.gov
# brufen - www.madesafe.govt.nz
    def make_coldandflu(self):
        return( "<h2 style = 'color:#9999ff;'>Cold-Flu</h2>"
                "<p>Flu and the common cold are both respiratory illnesses but they are caused by different viruses. Because these two types of illnesses have similar symptoms, it can be difficult to tell the difference between them based on symptoms alone. In general, flu is worse than the common cold, and symptoms are more intense. Colds are usually milder than flu. People with colds are more likely to have a runny or stuffy nose. Colds generally do not result in serious health problems, such as pneumonia, bacterial infections, or hospitalizations. Flu can have very serious associated complications.</p>"
                "<h3 style = 'color:#ff9999;'>BRUFEN</h3>"
                "<p>Brufen also relieves fever (high temperature). Although Brufen can relieve the symptoms of pain and inflammation, it will not cure your condition. Brufen contains the active ingredient ibuprofen. Ibuprofen belongs to a group of medicines called non-steroidal anti- inflammatory drugs (or NSAIDs).</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>1 - 2 yrs: drink 2.5ml three times a day.</p>"
                "<p>3 - 7 yrs: drink 5ml three times a day.</p>"
                "<p>8 - 12 yrs: drink 10 ml three times a day.</p>"
                "<h3 style = 'color:#ff9999;'>FLUDREX</h3>"
                "<p>Fludrex is in a form of a tablet that is needed to be swollowed along with some water to make it easier to make its ways down to the stomach. Fludrex is good at releiving cold & flu symptoms.</p>"
                "<h3 style = 'color:#ff9999;'>Dosgae</h3>"
                "<p>13 + yrs: swallow 1-2 tablets at a time, no more than 8 tablets a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Your blood has the same amount of salt in it as the ocean does.</p>")
# definition of cough&phlegm - www.medicinenet.com
# prospan - www.amcal.com.au
    def make_coughandphlegm(self):
        return( "<h2 style = 'color:#9999ff;'>Cough-Phlegm</h2>"
                "<p>A cough is a reflex action to clear your airways of mucus and irritants such as dust or smoke. It's rarely a sign of anything serious. A 'dry cough' means it's tickly and doesn't produce any phlegm (thick mucus). A 'chesty cough' means phlegm is produced to help clear your airways.</p>"
                "<h3 style = 'color:#ff9999;'>PROSPAN</h3>"
                "<p>Prospan by Helixia Cough Syrup. Prospan by Helixia is a naturally-sourced, over-the-counter cough syrup that is clinically proven to relieve coughs, loosen mucus & phlegm and alleviate the symptoms of chronic bronchitis.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>0 - 6 yrs: drink 2.5ml twice a day.</p>"
                "<p>7 - 12 yrs:  drink 5ml twice a day.</p>"
                "<p>12 + yrs: drink 5ml three times a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Babies are born with 300 bones - adults have 206.</p>")
# definition of dry eyes - www.aao.org
# refresh tears - www.refreshbrand.com
    def make_dryeyes(self):
        return( "<h2 style = 'color:#9999ff;'>Dry eyes</h2>"
            "<p>Our eyes need tears to stay healthy and comfortable. If your eyes do not produce enough tears, it is called dry eye. Dry eye is also when your eyes do not make the right type of tears or tear film.</p>"
            "<h3 style = 'color:#ff9999;'>Refresh Tears</h3>"
            "<p>Is an instantly moisturizes to provide immediate, soothing relief for dry, irritated eyes. It has many of the same healthy qualities as your own natural tears. Refresh Tears is an artificial tear that comes in a convenient multi-dose bottle and is safe to use as often as needed.</p>"
            "<h3 style = 'color:#ff9999;'>Dosage</h3>"
            "<p>10 + yrs: allow 1-2 eyedrops into your eye when needed.</p>"
            "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
            "<p>The heart pumps at least 9450 liters of blood a day.</p>")
# definition of ear infection - www.medicinenet.com
# apigen - www.ammanpharma.com
    def make_earinfection(self):
        return( "<h2 style = 'color:#9999ff;'>Ear infection</h2>"
                "<p>Acute middle ear infection, medically called acute otitis media is inflammation of the middle ear.</p>"
                "<h3 style = 'color:#ff9999;'>APIGEN</h3>"
                "<p>Apigen is used for the treatment of bacterial eye infections affecting eyelids, conjunctiva and cornea. For the prevention of eye infection after the removal of a foreign body. For the treatment of external ear bacterial infections (Otitis Externa). Effective against stubborn bacteria, such as: pseudomonas Aeruginosa.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>2 + yrs: allow 1-2 drops into the infected ear twice a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Fingernails grow 4 times as fast as your toe nails</p>")
# definition of headache - www.mayoclinic.org
# panadol actifast - www.medicines.org.uk
# blue eyes - www.aucklandeye.co.nz
    def make_headache(self):
        return( "<h2 style = 'color:#9999ff;'>Headache</h2>"
                "<p>Headache is pain in any region of the head. Headaches may occur on one or both sides of the head, be isolated to a certain location, radiate across the head from one point, or have a viselike quality. A headache may appear as a sharp pain, a throbbing sensation or a dull ache.</p>"
                "<h3 style = 'color:#ff9999;'>PANADOL ACTIFAST</h3>"
                "<p>Panadol ActiFast is a mild analgesic and antipyretic, and is recommended for the treatment of most painful and febrile conditions, for example, headache including migraine and tension headaches, toothache, backache, rheumatic and muscle pains, dysmenorrhoea, sore throat, and for relieving the fever, aches and pains.</p>"
                "<h3 style = 'color:#ff9999;'>Dosgae</h3>"
                "<p>10 - 15 yrs: dissolve one tablet into some warm water, no more than three times a day.</p>"
                "<p>16 + yrs: dissolve 1-2 tablets into some warm water, no more than three times a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Around 8 % of the worlds population have blue eyes.</p>")
# definition of heartburn - www.dictionary.com
# gaviscon - www.nhs.uk
# grey eyes - www.healthline.com
    def make_heartburn(self):
        return( "<h2 style = 'color:#9999ff;'>Heartburn</h2>"
                "<p> A burning sensation, usually centered in the middle of the chest near the sternum, caused by the reflux of acidic stomach fluids that enter the lower end of the esophagus. Also called acid reflux.</p>"
                "<h3 style = 'color:#ff9999;'>GAVISCON</h3>"
                "<p>Gaviscon can be used to treat heart burn (acid reflux) and indigestion. The medicine forms a protective layer that floats on top of the contents of your stomach. This stops stomach acid escaping up into your food pipe.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>Adults: drink around 15-30ml depending on intensity of acid reflux.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Only 1 - 2 % of the population have grey eyes.</p>")
# definition of high fever - en.wikipedia.org
# parafast et 1000 - www.1mg.com
# brown eyes - www.healthline.com
    def make_highfever(self):
        return( "<h2 style = 'color:#9999ff;'>High Fever</h2>"
                "<p>Fever, also referred to as pyrexia, is defined as having a temperature above the normal range due to an increase in the body's temperature set point. There is not a single agreed-upon upper limit for normal temperature with sources using values between 37.2 and 38.3 °C (99.0 and 100.9 °F) in humans.</p>"
                "<h3 style = 'color:#ff9999;'>BRUFEN</h3>"
                "<p>Brufen also relieves fever (high temperature). Although Brufen can relieve the symptoms of pain and inflammation, it will not cure your condition. Brufen contains the active ingredient ibuprofen. Ibuprofen belongs to a group of medicines called non-steroidal anti- inflammatory drugs (or NSAIDs).</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>1 - 2 yrs: drink 2.5ml three times a day.</p>"
                "<p>3 - 7 yrs: drink 5ml three times a day..</p>"
                "<p>8 - 12 yrs: drink 10 ml three times a day.</p>"
                "<h3 style = 'color:#ff9999;'>PARAFAST ET 1000</h3>"
                "<p>Parafast 1000mg is a painkiller used to treat aches and pains. It works by blocking chemical messengers in the brain that tell us we have pain. It is effective in relieving pain caused by headache, migraine, nerve pain, toothache, sore throat, arthritis and muscle aches.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>3 - 12 yrs: drink 500mg dissolved into some warm water twice a day.</p>"
                "<p>13 + yrs: drink 1000mg dissolved into some water twice a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Around 79 % of the entire population have brown eyes.</p>")
# definition of joint sprain - www.mayoclinic.org
# 99.9% alike - blogs.ancestry.com
    def make_jointsprain(self):
        return( "<h2 style = 'color:#9999ff;'>Joint sprain</h2>"
                "<p>A sprain is a stretching or tearing of ligaments — the tough bands of fibrous tissue that connect two bones together in your joints. The most common location for a sprain is in your ankle. Initial treatment includes rest, ice, compression and elevation.</p>"
                "<h3 style = 'color:#ff9999;'>FAST RELIEF SPRAY</h3>"
                "<p>The applied spray is absorbed through the skin and goes right into the affected tissues. It works by reducing pain only on the affected area of the body without altering other sensitive areas such as the digestive tract.</p>"
                "<h3 style = 'color:#ff9999;'>Directions</h3>"
                "<p>Apply some of the fast relief spray on the sprainted area.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>We are all 99.9% alike.</p>")
# definition of minor muscle/joint pain - www.mayoclinic.org
# salonpas - www.webmd.com
    def make_minormuscleorjointpain(self):
        return( "<h2 style = 'color:#9999ff;'>Minor muscle/joint pain</h2>"
                "<p>Joint pain can be discomfort, pain or inflammation arising from any part of a joint — including cartilage, bone, ligaments, tendons or muscles. Most commonly, however, joint pain refers to arthritis or arthralgia, which is inflammation or pain from within the joint itself.</p>"
                "<h3 style = 'color:#ff9999;'>SALONPAS</h3>"
                "<p>This medication is used to treat minor aches and pains of the muscles/joints (e.g., arthritis, backache, sprains). Capsaicin works by decreasing a certain natural substance in your body (substance P) that helps pass pain signals to the brain.</p>"
                "<h3 style = 'color:#ff9999;'>Directions</h3>"
                "<p>Adhere a patch of salonpas to the targeted area.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>The smallest bone in your body is in your ears.</p>")
# definition of pink eye - www.webmd.com
# 12% black&white - www.nectarsleep.com
    def make_pinkeye(self):
        return( "<h2 style = 'color:#9999ff;'>Pink eye</h2>"
                "<p>Conjunctivitis, also known as pinkeye, is an inflammation of the conjunctiva. The conjunctiva is the thin clear tissue that lies over the white part of the eye and lines the inside of the eyelid.</p>"
                "<h3 style = 'color:#ff9999;'>APIGEN</h3>"
                "<p>For the treatment of bacterial eye infections affecting eyelids, conjunctiva and cornea. For the prevention of eye infection after the removal of a foreign body. For the treatment of external ear bacterial infections (Otitis Externa). Effective against stubborn bacteria, such as: pseudomonas Aeruginosa.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>Allow 1-2 drops into your eye twice a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>12% of the people dream in black and white.</p>")
# definition of pregnancy vitamin-B - www.healthline.com
# folic acid - www.webmd.com
    def make_pregnancyvitaminB(self):
        return( "<h2 style = 'color:#9999ff;'>Pregnancy Vitamin-B</h2>"
                "<p>Maintaining a well-balanced diet is one of the best things you can do for your body. This is especially true when you are pregnant. Foods rich in the eight B vitamins (known as B complex) play an important role in supporting a healthy pregnancy.Mary L. Rosser, MD, PhD, attending physician at the Department of Obstetrics and Gynecology and Women Health at Montefiore Medical Center, Bronx, New York, explains that, 'they keep your body strong while your baby is growing. They also change food into energy, giving you that needed boost during your pregnancy.' This natural energy lift will help if you are feeling tired during your first and third trimesters.</p>"
                "<h3 style = 'color:#ff9999;'>FOLIC ACID</h3>"
                "<p>Folic acid is a man-made form of a B vitamin called folate. Folate plays an important role in the production of red blood cells and helps your baby's neural tube develop into her brain and spinal cord. The best food sources of folic acid are fortified cereals.</p>"
                "<h3 style = 'color:#ff9999;'>Dosage</h3>"
                "<p>Swallow 1 tablet of folic acid followed by water once a day.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Laying the blood vessele from end to end - it can circle the globe.</p>")
# definition of runny nose - www.mayoclinic.org
# eye fact - versanhealth.com
    def make_runnynose(self):
        return( "<h2 style = 'color:#9999ff;'>Runny nose</h2>"
                "<p>A runny nose is excess nasal drainage. It may be a thin clear fluid, thick mucus or something in between. The drainage may run out of your nose, down the back of your throat or both. The terms 'rhinorrhea' and 'rhinitis' are often used to refer to a runny nose.</p>"
                "<h3 style = 'color:#ff9999;'>STERIMAR SPRAY</h3>"
                "<p>The spray uses a microdiffusion system to produce a gentle fine spray of the sea water onto the lining of the nose. These fine droplets soften and loosen the nasal mucus, which you can then blow out along with any bacteria or viruses.</p>"
                "<h3 style = 'color:#ff9999;'>Directions</h3>"
                "<p>Allow some of the liquid spray into your nostrils.</p>"
                "<h3 style = 'color:#009999;'> Fun Fact:</h3>"
                "<p>Your eye focuses on 50 different objects every second.</p>")
# definition of teething - www.merriam-webster.com
# coca-cola - www.pharmacytimes.com
    def make_teething(self):
        return( "<h2 style = 'color:#9999ff;'>Teething</h2>"
                "<p>The first growth of teeth. The phenomena accompanying growth of teeth through the gums.</p>"
                "<h3 style = 'color:#ff9999;'>DAD TEETHING GEL</h3>"
                "<p>Dentinox Teething Gel contains the active ingredients lidocaine and cetylpyridinium. Lidocaine is one of a group of medicines called local anesthetics, which numb pain. Cetylpyridinium is an antiseptic that is used to treat minor wounds and minor infections of the mouth.</p>"
                "<h3 style = 'color:#ff9999;'>Directions</h3>"
                "<p>Apply some gel to the active site of teething.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Coca-Cola was invented by a pharmacist named John Pemberton.</p>")
# definition of toothache - en.wikipedia.org
# fact - www.pharmacytimes.com
    def make_toothache(self):
        return( "<h2 style = 'color:#9999ff;'>Toothache</h2>"
                "<p>Toothache, also known as dental pain, is pain in the teeth or their supporting structures, caused by dental diseases or pain referred to the teeth by non-dental diseases. When severe it may impact sleep, eating, and other daily activities.</p>"
                "<h3 style = 'color:#ff9999;'>SAVOY TOOTHACHE DROPS</h3>"
                "<p>Benzocaine is used short term to relieve pain from minor mouth problems (such as toothache, canker sores, sore gums/throat, mouth/gum injury). It is a local anesthetic that works by numbing the painful area.</p>"
                "<h3 style = 'color:#ff9999;'>Directions</h3>"
                "<p>Dip in a q-tip, and apply it on pain site.</p>"
                "<h3 style = 'color:#009999;'>Fun Fact:</h3>"
                "<p>Benjamin Franklin was a pharmacist, while Agatha Christie was a pharmacy technician.</p>")


    def do_GET(self):
        print(self.path)

        if self.path == "/allergies":
            page_html = self.make_header() + self.make_allergies() + self.make_footer()

        elif self.path == "/asthma":
            page_html = self.make_header() + self.make_asthma() + self.make_footer()

        elif self.path == "/coldandflu":
            page_html = self.make_header() + self.make_coldandflu() + self.make_footer()

        elif self.path == "/coughandphlegm":
             page_html = self.make_header() + self.make_coughandphlegm() + self.make_footer()

        elif self.path == "/dryeyes":
             page_html = self.make_header() + self.make_dryeyes() + self.make_footer()

        elif self.path == "/earinfection":
             page_html = self.make_header() + self.make_earinfection() + self.make_footer()

        elif self.path == "/headache":
             page_html = self.make_header() + self.make_headache() + self.make_footer()

        elif self.path == "/heartburn":
             page_html = self.make_header() + self.make_heartburn() + self.make_footer()

        elif self.path == "/highfever":
             page_html = self.make_header() + self.make_highfever() + self.make_footer()

        elif self.path == "/jointsprain":
             page_html = self.make_header() + self.make_jointsprain() + self.make_footer()

        elif self.path == "/minormuscleorjointpain":
             page_html = self.make_header() + self.make_minormuscleorjointpain() + self.make_footer()

        elif self.path == "/pinkeye":
             page_html = self.make_header() + self.make_pinkeye() + self.make_footer()

        elif self.path == "/pregnancyvitaminB":
             page_html = self.make_header() + self.make_pregnancyvitaminB() + self.make_footer()

        elif self.path == "/runnynose":
             page_html = self.make_header() + self.make_runnynose() + self.make_footer()

        elif self.path == "/teething":
             page_html = self.make_header() + self.make_teething() + self.make_footer()

        elif self.path == "/toothache":
             page_html = self.make_header() + self.make_toothache() + self.make_footer()

        else:
             page_html = self.make_header() + self.make_home() + self.make_footer()


        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(page_html.encode())

myServer = HTTPServer(('0.0.0.0', 9011), OnlinePharmacy)
myServer.serve_forever()