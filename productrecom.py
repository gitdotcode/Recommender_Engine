import pandas as pd
import streamlit as st
import pickle

product_dict = pickle.load(open("product_dict.pkl", 'rb'))
sim_dict = pickle.load(open("sim_dict.pkl", 'rb'))
products = pd.DataFrame(product_dict)
sim = pd.DataFrame(sim_dict)


def main():
    st.title('Product Recommender Engine')
    selected_product = st.selectbox('Select Product ID',products['Product_ID'].values)
    menu = ['Home', 'Recommend', 'Description','Product Link']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader('Home')
        st.dataframe(products)

    elif choice == "Recommend":
        st.subheader("Recommend Product")

        # search_term = st.text_input("Select Product ID")
        def get_reco(selected_product):
            tem = list(sim.sort_values([selected_product], ascending=False).head(100).index)
            product_list = list(products[products['Product_ID'].isin(tem)]['product_name'])
            recommend_list = set(product_list) - set(products[products['Product_ID'] == selected_product]['product_name'])
            return recommend_list

        if st.button('Recommend'):

            try:
                result = get_reco(selected_product)
            except:
                result = 'Not Found'

            st.write(result)

    elif choice == 'Product Link':
        st.subheader('Product Link')
        st.write(products['product_link'])


            # rec = recommend(selected_product)
            # st.write(rec)

        # def recommend(Product_ID):
        #     tem = list(products.sort_values([Product_ID], ascending=False).head(100).index)
        #     product_list = list(products[products['Product_ID'].isin(tem)]['product_name'])
        #     recommend_list = set(product_list) - set(products[products['Product_ID'] == Product_ID]['product_name'])
        #     return recommend_list

        # if st.button('Recommend'):
        #     if search_term is not None:
        #         pass

    else:
        st.subheader('Description')
        st.text('Recommender Engine for various e-shopping categories. Thank You :)')


if __name__ == '__main__':
    main()

# def recommend(Product_ID):
#     tem = list(products.sort_values([Product_ID], ascending=False).head(100).index)
#     product_list = list(products[products['Product_ID'].isin(tem)]['product_name'])
#     recommend_list = set(product_list) - set(products[products['Product_ID'] == Product_ID]['product_name'])
#
#     # if recommend_list == set():
#     #     return 'Look for more similarity'
#     return recommend_list

# def recommend(producT):
#     product_index = products[products['product_name'] == producT].index[0]
#     distances = similarity[product_index]
#     product_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]


#     recommend_products = []
#     for i in product_list:
#         # product_id = products.iloc[i[0]].Product_ID
#         recommend_products.append(products.iloc[i[0]].product_name)
#     return recommend_products
#

#
# st.title('Product Recommender')
#
# with st.sidebar.form("Choose Product"):
#     selected_product = st.selectbox(
#         'Select Product ID',
#         products['Product_ID'].values)
#
#     selected_product_link = st.selectbox(
#         'product link',
#         products['product_link'].values)


#
# if st.button('link'):
#     st.write(product_link)
#
#
#
# if st.button('Recommend'):
#     recommend(selected_product)
#     st.write(selected_product)
