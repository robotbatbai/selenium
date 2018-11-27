# coding:utf-8
class duvetClass:
    size = [['Twin',78.5,98],['Full',84.5,105.6],['Queen',89.5,111.9],['King',98.5,123],['California King',98.5,123]]
    taglist = "tropical Duvet Cover Set, bedclothes, bedding sets, bed linen, Bedspread, bedcover, bed sheets, bedspread sets, luxury bedding sets"
    productType = "duvet cover, bedding sets"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Tropical-Duvet-Cover-Set/1160570_513276359.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<div>
            <h3><strong><span>UPGRADE YOUR LIFESTYLE WITH TRENDY BEDCOVER</span></strong></h3>
            <p><span>Trends change a lot with the passage of time. That’s why we make sure to bring you the trendiest fashionable bed covers.</span></p>
            <h3><strong><span>SLEEP IN AVANT-GARDE STYLE</span></strong></h3>
            <p><span>This bedding set has the most fascinating catchy look, with colourful artwork that leaves everyone staring in awe. Let your bed cover remind you to <em>laugh, live every moment</em> and <em>love beyond words</em>.</span></p>
            <h3><strong><span>UPDATE YOUR BEDROOM APPEAL</span></strong></h3>
            <p><span>Give your bedroom a supreme trendy look with this bed cover that reflects your stylish and happy-go-lucky lifestyle. Your exclusive tastes can only be satisfied with a unique microfiber bed cover like this one.</span></p>
            <h3><strong><span>MADE WITH 100% PURE AND SUPERIOR FABRIC</span></strong></h3>
            The quality of this bed cover is owed to the use of microfiber material. That’s what makes it not only good-looking, but also comfortable, soft, relaxing, and surprisingly long-lasting. We give 100% guarantee to our customers when it comes to quality and durability. This wrinkle-free and fade-resistant bed cover set is easy to use, easy to care for and easy to wash.
            <div>
                <br />
                <h3><strong><span>BED SET INCLUDES: 1* DUVET COVER 2* PILLOWCASES</span></strong></h3>
            </div>
            </div>"""
    body2 = """<h3><strong><span>SWEET BEDCOVER FOR YOUR SWEET DREAMS</span></strong></h3>
        <p><span>When anyone enters a bedroom, the first thing they notice is the bed. This is precisely why an aesthetic bed cover with gorgeous design is a must.</span></p>
        <h3><strong><span>A BEDCOVER YOU CAN’T TAKE YOUR EYES OFF</span></strong></h3>
        <p><span>With a remarkable cluster of brilliant colours and fancy artwork, this bed set highlights the impression of your bedroom in an exquisite manner. The impressive arrangement of sundry designs in catchy colors and pattern make it a magnificent view for all.</span></p>
        <h3><strong><span>SUPERIOR FABRIC QUALITY THAT YOU DESERVE</span></strong></h3>
        <p>Our premium quality bed covers are made of microfiber, and that’s what makes them special. Microfiber bed covers offer unmatched softness and durability. What makes this bed cover unique from the rest are its qualities of wrinkle and fade resistance. The 1 quilt cover and 2 matching pillowcases, all are made of 100% pure and premier microfiber for luxurious feel. You’ll never want to leave your bed!</p>
        <br />
        <h3><strong><span>BED SET INCLUDES: 1* DUVET COVER 2* PILLOWCASES</span></strong></h3>"""
    body3 = """<h3><strong>FASHIONABLE BED COVERS<span> FOR ULTIMATE COMFORT AND QUALITY</span></strong></h3>
        <p><span>We all place our comfort at top priority, especially in the bedroom. At the close of a hectic daily routine, all we want is to snuggle in our comfortable bed.  Well, your bed can’t be the ultimate relaxation spot without a comfortable bedcover!</span></p>
        <h3><strong><span>LIE DOWN ON LUXURY DUVET</span></strong></h3>
        <p><span>This bed set is made of the most comfortable and soft fabric: microfiber cloth. With 100% satisfaction guarantee, we deliver our customers the finest quality bed covers that will redefine comfort.</span></p>
        <h3><strong><span>EXPERIENCE PREMIUM QUALITY BED COVERS</span></strong></h3>
        <p><span>Other materials make the bedcover sheets irritable after a time of use, but microfiber bed covers are exceptional. No matter how often you use it, it will feel comfy and new every time. Softness and strength come together in microfiber fabric to produce luxurious comfort and tough durability.</span></p>
        <h3><strong><span>USE AGAIN AND AGAIN</span></strong></h3>
        <p>Microfiber fabric worn-out and the colours, print and textile are guaranteed to work longer and remain intact. So, never lose your comfort with this Bohemian bedcover. With tender washing and line dry, you can use this bedcover with ultimate assurance.</p>
        <br />
        <h3><strong><span>BED SET INCLUDES:  1* DUVET COVER 2* PILLOWCASES</span></strong></h3>"""
    body4 = """<div>
            <h3><strong>QUALITY BEDCOVER<span> FOR YOUR BEDROOM.</span></strong></h3>
            <p><span>Are you worried about the quality of bedcovers because of your sensitive skin? The solution is here.</span></p>
            <h3><strong><span>THE BEST BED COVER FOR SENSITIVE SKIN.</span></strong></h3>
            <p><span>Our 100% microfiber bed cover is made of the finest material that caresses your skin with the most gentle and soft touch. Microfiber is the best fabric for sensitive skin which is prone to allergies or skin problems.</span></p>
            <h3><strong><span>ELEGANCE AND EXCELLENCE IN ONE BED COVER.</span></strong></h3>
            <p><span>This bedding set is designed to stand out in terms of aesthetics as well as class. Washing such printed bed covers is usually difficult because machines fade the colours and impair the quality. But, with this high-quality bedcover, you don’t need to worry about because its charm and quality will not fade away.</span></p>
            <h3><strong><span>FEELS GOOD AS NEW, EVERY SINGLE TIME.</span></strong></h3>
            <p><span>Microfiber cloth is specially chosen for our bed covers because it is wrinkle- and fade-resistant with 100% guarantee for enduring use. While other bed covers become rough, dull and threadbare over time, the Bohemian bed cover is threaded to perfection and stays that way for years.</span></p>
            But remember not to use bleach, wash it gently, and let it cool tumble and line dry for the long-lasting usage.</div>
        <div></div>
        <div>
            <h3><strong><span>BED SET INCLUDES:  1* DUVET COVER 2* PILLOWCASES</span></strong></h3>
        </div>"""
    body = [body1,body2,body3,body4]
################################## blanket and throws ############################
class blanketClass:
    size = [['Throw(50"x60")',39.3,49.5],['Twin(60"x80")',49.2,61.5]]
    taglist = "fuzzy blankets, throw blankets, throws and blankets, plush blankets, sofa throws, couch throws"
    productType = "throws and blankets"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Throw-Blankets/1160570_513431825/1.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<p><strong>Product Description</strong></p>
<p><strong> Material: </strong>Sherpa Fleece</p>
<p> <strong> Feature: </strong> Portable,Anti-Pilling,Wearable </p>
<p> <strong> Season: </strong> Spring/Autumn </p>
<p> <strong> Technics: </strong> Woven </p>
<p> This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great companion.Our fabric is strong, durable, and if cared for properly, will be long lasting. </p>"""
    body2 = """<p><strong>Product Description</strong></p>
<p><strong> Material: </strong>Sherpa Fleece</p>
<p> <strong> Feature: </strong> Portable,Anti-Pilling,Wearable </p>
<p> <strong> Season: </strong> Spring/Autumn </p>
<p> <strong> Technics: </strong> Woven </p>
<p> This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great companion.Our fabric is strong, durable, and if cared for properly, will be long lasting. </p>"""
    body3 = """<p><strong>Product Description</strong></p>
<p><strong> Material: </strong>Sherpa Fleece</p>
<p> <strong> Feature: </strong> Portable,Anti-Pilling,Wearable </p>
<p> <strong> Season: </strong> Spring/Autumn </p>
<p> <strong> Technics: </strong> Woven </p>
<p> This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great companion.Our fabric is strong, durable, and if cared for properly, will be long lasting. </p>"""
    body4 = """<p><strong>Product Description</strong></p>
<p><strong> Material: </strong>Sherpa Fleece</p>
<p> <strong> Feature: </strong> Portable,Anti-Pilling,Wearable </p>
<p> <strong> Season: </strong> Spring/Autumn </p>
<p> <strong> Technics: </strong> Woven </p>
<p> This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great companion.Our fabric is strong, durable, and if cared for properly, will be long lasting. </p>"""
    body = [body1,body2,body3,body4]
##################################### hooded blanket ###########################################
class hoodedClass():
    size = [['Adult(60"x80")',49.6,62.5],['Kid(50"x60")',39.8,49.5]]
    taglist = "blankets, printed blanket, hooded Blankets"
    productType = "Hooded Blanket"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Hooded-Blankets/1160570_513431826.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body2 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body3 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body4 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body = [body1,body2,body3,body4]
##################################### Mats and Rugs ###########################################
class matClass():
    size = [['15.7"x23.6"',23.8,31.5],['20"x32"',29.6,37.5]]
    taglist = "blankets, printed blanket, hooded Blankets"
    productType = "Mats and Rugs"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Mat-Rugs/1160570_508046227.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body2 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body3 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body4 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body = [body1,body2,body3,body4]
##################################### table cloth ###########################################
class tableclothClass():
    size = [['15.7"x23.6"',23.8,31.5],['20"x32"',29.6,37.5]]
    taglist = "blankets, printed blanket, hooded Blankets"
    productType = "Mats and Rugs"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Table-Cloth/1160570_512452744.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body2 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body3 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body4 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body = [body1,body2,body3,body4]

##################################### round carpet ###########################################
class roundcarpetClass():
    size = [['15.7"x23.6"',23.8,31.5],['20"x32"',29.6,37.5]]
    taglist = "blankets, printed blanket, hooded Blankets"
    productType = "Mats and Rugs"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Round-Carpet/1160570_514383374.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body2 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body3 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body4 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body = [body1,body2,body3,body4]

##################################### bathroom match ###########################################
class bathromClass():
    size = [['15.7"x23.6"',23.8,31.5],['20"x32"',29.6,37.5]]
    taglist = "blankets, printed blanket, hooded Blankets"
    productType = "Mats and Rugs"
    # start from this url 
    url = ['https://www.aliexpress.com/store/product/BeddingOutlet-Watercolor-Dreamcatcher-Bedding-Set-King-Blue-Bedclothes-for-Adult-Kids-Luxury-Chinese-Style-Quilt-Cover/1160570_32831117756.html']
    urls = 'https://beddingoutlet.aliexpress.com/store/group/Bathroom-Mat-Set/1160570_514371716.html'

    # list keyword filter from title 
    replaceList = ['BeddingOutlet','Chinese','King ', 'Blue ','for Adult Kids ','3 Pcs','King ','Queen ','Dropship ']
    spiltImage = "#j-image-thumb-list img::attr(src)"
    title = "h1.product-name::text"
    
    # get list page 
    pageDetail = "ul.items-list div.pic"
    nextPage = "a.ui-pagination-next::attr(href)"

    #body list 
    body1 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body2 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body3 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body4 = """<p><strong>Product Description</strong></p>
<p><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Material:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i3.41be44efaaI66d">Sherpa Fleece</span></p>
<p><span class="propery-des" title="Sherpa Fleece"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Feature:</span></strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i5.41be44efaaI66d">Portable,Anti-Pilling,Wearable</span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i6.41be44efaaI66d">Season:</span></strong><span class="propery-des" title="Spring/Autumn">Spring/Autumn</span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><strong><span class="propery-title" data-spm-anchor-id="2114.10010108.0.i8.41be44efaaI66d">Technics:</span></strong><span class="propery-des" title="Woven">Woven</span></span></span></span></p>
<p><span class="propery-des" title="Sherpa Fleece"><span class="propery-des" title="Wearable,Anti-Pilling,Portable"><span class="propery-des" title="Spring/Autumn"><span class="propery-des" title="Woven"><span>This blanket is perfect for anything you need. While you're sitting on the couch and watching a movie, or in your bed on a cold night, this blanket is sure to be a great  companion.Our fabric is strong, durable, and if cared for properly, will be long lasting.</span></span></span></span></span></p>"""
    body = [body1,body2,body3,body4]



    