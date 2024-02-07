import streamlit as st
import pandas as pd
import time
from PIL import Image
# import pandas as pd
#
# # Sample DataFrame
# data = {'Text_Column': ['apple', 'banana', 'grape', 'cherry', 'pineapple']}
# df = pd.DataFrame(data)

# Using regex to filter rows based on a pattern in the 'Text_Column'


# print(filtered_df)
# Set the background color using set_page_config
tab1_table = pd.read_csv(r"upsc_book.csv", encoding='latin1')
tab2_table=pd.DataFrame({"Books":["Polity"],"Writer":["LakshiKant"],"Price":[300],"Discount":[20]})
tab3_table=pd.DataFrame({"Books":["Polity"],"Writer":["LakshiKant"],"Price":[300],"Discount":[20]})
tab4_table=pd.DataFrame({"Books":["Polity"],"Writer":["LakshiKant"],"Price":[300],"Discount":[20]})

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded")
#     theme=[theme]
# base="light"
# font="monospace"

# page_color="white"
st.title(":red[Vikas Book Shop At Paharia Varanai]")

    # Set your desired background color

# st.balloons()
st.snow()
image_paths = ["im.jpg","im.jpg","im.jpg"]

# Function to display images in a running manner
# def display_running_images(images):
#     for image_path in images:
#         # Open and display the image
#         a=
#         # Wait for a short duration before displaying the next image
#         time.sleep(2)  # Adjust the sleep duration as needed
#
# # Run the function to display images
# display_running_images(image_paths)
text_shop = """Best price book seller all types of books are available with correct discount
 rate. UPSC books, SSC books, and other important books are available.
"""

def green_text_run(text_shop):
    for word in text_shop.split():
        green_word =   word + " "  # Set text color to green
        yield f":rainbow[{green_word}] "
        time.sleep(0.1)
with st.sidebar:
    with st.expander(":red[About Us]"):
        st.write(":red[Contact number:9005865087]")
        gmail="vksujma21059005854@gmail.com"
        st.markdown(f":red[**Gmail:**]{gmail}")
        link="https://github.com/vksujma210590058?tab=repositories"
        st.markdown(f":red[**Location:**]{link}")

    if st.button("click"):
        st.write(green_text_run(text_shop))
        st.image(r"im.jpg",caption="Shop")
tab1,tab2,tab3,tab4=st.tabs(["Upsc Csc Books","Ssc Books","Defence Books","Others Books"])

with tab1:
    col_intro1=st.container(height=500,border=True)
    col_intro1.image("book_shop.jpg",caption="Book Shop")
    # col_intro=st.columns(1)
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    # with col_intro:
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")

        col1_con.image("book.jpg",caption="Book")

        # List of image paths
        # image_paths = ["im.jpg", "im.jpg", "im.jpg"]
        # col1_con.image_pressore
        # Function to display images in a running manner


# Run the function to display images


    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("book2.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("book.jpg",caption="Book")
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")
        col1_con.image("im.jpg",caption="Book")
    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("im.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("im.jpg",caption="Book")
    with tab1.expander(":red[More Books]"):
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
            col1_con.image("im.jpg",caption="Book")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
            col2_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
            col3_con.image("im.jpg",caption="Book")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
            col4_con.image("im.jpg",caption="Book")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
            col1_con.image("im.jpg",caption="Book")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
            col2_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
            col3_con.image("im.jpg",caption="Book")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
            col4_con.image("im.jpg",caption="Book")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
            col1_con.image("im.jpg",caption="Book")
        with col2:
            col2_con=st.container(height=300,border=True)
            col2_con.image("im.jpg",caption="Book")
            col2_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
            col3_con.image("im.jpg",caption="Book")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
            col4_con.image("im.jpg",caption="Book")
    with tab1.expander(":red[Search More Books]"):
        if st.button(label=":red[Click me to see All Books of Upsc]",key="asdf"):
            st.write(tab1_table)
        book_want_user=st.chat_input(placeholder="Book name That you want to buy",key="chat_input_tab1")
        if book_want_user is not None:
            pattern = f'.*{book_want_user}'  # This regex pattern matches any string ending with 'ple'
            filtered_df = tab1_table[tab1_table['Books'].str.contains(pattern, regex=True)]
            # search_book=tab1_table[tab1_table["Books"]==book_want_user]
            st.write(filtered_df)
        # text_selectbox="less than "
        price=[None,250,350,450,1000]
        # joined_text=text_selectbox+str
        select_search_box=st.selectbox(label=":rainbow[Upsc book on the based on Price]:red[ less than]",options=price)
        if select_search_box is not None:
            tab1_table[(tab1_table["Price"]>=select_search_box-100)&(tab1_table["Price"]<=select_search_box)]

    st.title(":rainbow[Happy Happy Day God With You Always]")
    with tab1.expander(":green[Feedback or any that is not available]"):
        st.markdown(""":rainbow[Feedback or anything that you need but not available in our store
        And We will add that book in our store]""")
        Upsc_book_not=st.chat_input("That Upsc Book you need but not in Store")
    with st.container(height=250,border=True):
        col1_w,col2_w,col3_w,col4_w=st.columns(4)
        col1_w.markdown("""HI my name is vikas maurya 
        this si my book shop  website and at 
        our shoop evry book is avaibale at 
        correct price with correct 
        discount
        :microphone:**www.facebook.com**""")
        col2_w.markdown("""HI my name is vikas maurya 
        this si my book shop  website and at 
        our shoop evry book is avaibale at 
        correct price with correct
         discount
        :house_buildings:**https://www.google.com/maps/@25.4358011,81.846311,10z/data=!4m2!7m1!2e1?entry=ttu**""")
        col3_w.markdown("""HI my name is vikas maurya 
        this si my book shop  website and at 
        our shoop evry book is avaibale at 
        correct price with correct discount
        :iphone:**9005865087**""")
        col4_w.markdown("""HI my name is vikas maurya 
        this si my book shop  website and at 
        our shoop evry book is avaibale at 
        correct price with correct discount
        :books:**vksuj210590058545@gmail.com**""")




#FROM  HERE WE ARE GOING TO WRITE  THE FOR THE SECOND TAB
with tab2:
    col_intro1=st.container(height=500,border=True)
    col_intro1.image("book_shop.jpg",caption="Book Shop")
    # col_intro=st.columns(1)
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    # with col_intro:
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")

        col1_con.image("book.jpg",caption="Book")

        # List of image paths
        # image_paths = ["im.jpg", "im.jpg", "im.jpg"]
        # col1_con.image_pressore
        # Function to display images in a running manner


    # Run the function to display images


    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("book2.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("book.jpg",caption="Book")
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")
        col1_con.image("im.jpg",caption="Book")
    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("im.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("im.jpg",caption="Book")
    with tab2.expander(":red[More Books]"):
        col1,col2,col3,col4=st.columns(4)
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
    with tab2.expander(":red[Search More Books]"):
        if st.button("Click me to see All Books Ssc"):
            st.write(tab2_table)
        book_want_user=st.chat_input(placeholder="Ssc Book name That you want to buy")

        if book_want_user is not None:
            search_book=tab1_table[tab1_table["Books"]==book_want_user]
            st.write(search_book)
        price=[None,250,350,450,1000]
        # joined_text=text_selectbox+str
        select_search_box=st.selectbox(label=":rainbow[Ssc book on the based on Price]:red[ less than]",options=price)
        if select_search_box is not None:
            tab1_table[(tab1_table["Price"]>=select_search_box-100)&(tab1_table["Price"]<=select_search_box)]
    st.write(":rainbow[Happy Happy Day God With You Always]")

    with tab2.expander(":green[Feedback]"):
        st.write(":rainbow[Feedback or anything that you need but not available in our store\nAnd We will add that book in our store]")
        Ssc_book_not=st.chat_input("That Ssc  Book you need but not in Store")
# FROM HERE WE ARE GOING TO WRITE FROM THE TAB 3
with tab3:
    col_intro1=st.container(height=500,border=True)
    col_intro1.image("book_shop.jpg",caption="Book Shop")
    # col_intro=st.columns(1)
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    # with col_intro:
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")

        col1_con.image("book.jpg",caption="Book")

        # List of image paths
        # image_paths = ["im.jpg", "im.jpg", "im.jpg"]
        # col1_con.image_pressore
        # Function to display images in a running manner


    # Run the function to display images


    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("book2.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("book.jpg",caption="Book")
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")
        col1_con.image("im.jpg",caption="Book")
    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("im.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("im.jpg",caption="Book")
    with tab3.expander(":red[More Books]"):
        col1,col2,col3,col4=st.columns(4)
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
    with tab3.expander(":red[Search More Books]"):
        if st.button("Click me to see All Books Defence"):
            st.write(tab3_table)
        book_want_user=st.chat_input(placeholder="Defence Book name That you want to buy")

        if book_want_user is not None:
            search_book=tab1_table[tab1_table["Books"]==book_want_user]
            st.write(search_book)
        price=[None,250,350,450,1000]
        # joined_text=text_selectbox+str
        select_search_box=st.selectbox(label=":rainbow[Defence book on the based on Price]:red[ less than]",options=price)
        if select_search_box is not None:
            tab1_table[(tab1_table["Price"]>=select_search_box-100)&(tab1_table["Price"]<=select_search_box)]

    st.title(":rainbow[Happy Happy Day God With You Always]")
    with tab3.expander("Feedback"):
        st.write(":rainbow[Feedback or anything that you need but not available in our store\nAnd We will add that book in our store]")
        Defence_book_not=st.chat_input("That Defence Book you need but not in Store")

# FROM HERE WE ARE GOING TO  WIRTE THE CODE FOR THE  TAB4
with tab4:
    col_intro1=st.container(height=500,border=True)
    col_intro1.image("book_shop.jpg",caption="Book Shop")
    # col_intro=st.columns(1)
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    # with col_intro:
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")

        col1_con.image("book.jpg",caption="Book")

        # List of image paths
        # image_paths = ["im.jpg", "im.jpg", "im.jpg"]
        # col1_con.image_pressore
        # Function to display images in a running manner


    # Run the function to display images


    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("book2.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("book.jpg",caption="Book")
    with col1:
        col1_con=st.container(height=300,border=True)
        col1_con.write(":rainbow[hello]")
        col1_con.image("im.jpg",caption="Book")
    with col2:
        col2_con=st.container(height=300,border=True)
        col1_con.image("im.jpg",caption="Book")
        col2_con.image("im.jpg",caption="Book")
    with col3:
        col3_con=st.container(height=300,border=True)
        col3_con.write(":rainbow[hello]")
        col3_con.image("im.jpg",caption="Book")
    with col4:
        col4_con=st.container(height=300,border=True)
        col4_con.write(":rainbow[hello]")
        col4_con.image("im.jpg",caption="Book")
    with tab4.expander(":red[More Books]"):
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
        with col1:
            col1_con=st.container(height=300,border=True)
            col1_con.write(":rainbow[hello]")
        with col2:
            col2_con=st.container(height=300,border=True)
            col1_con.image("im.jpg",caption="Book")
        with col3:
            col3_con=st.container(height=300,border=True)
            col3_con.write(":rainbow[hello]")
        with col4:
            col4_con=st.container(height=300,border=True)
            col4_con.write(":rainbow[hello]")
    with tab4.expander(":red[Search More Books]"):
        if st.button("Click me to see All Books other"):
            st.write(tab4_table)
        book_want_user=st.chat_input(placeholder="Other Book name That you want to buy")
        if book_want_user is not None:
            search_book=tab1_table[tab1_table["Books"]==book_want_user]
            st.write(search_book)
        price=[None,250,350,450,1000]
        # joined_text=text_selectbox+str
        select_search_box=st.selectbox(label=":rainbow[Other book on the based on Price]:red[ less than]",options=price)
        if select_search_box is not None:
            tab1_table[(tab1_table["Price"]>=select_search_box-100)&(tab1_table["Price"]<=select_search_box)]
    st.title(":rainbow[Happy Happy Day God With You Always]")

    with tab4.expander(":green[Feedback]"):
        st.write(":rainbow[Feedback or anything that you need but not available in our store\nAnd We will add that book in our store]")
        Ssc_book_not=st.chat_input("That Other Book you need but not in Store")

# COLLECT THE IN FOMATION FROM THE USER AND  SAVE IT
# FOR THE TEN DAYS AND AND
# IN THE TABLE FORM
# GIVE GMAIL AND POSSWORD AND SAVE OR DOWNLOAD IT AND AND DELTE IT  OFTER TEN DAY