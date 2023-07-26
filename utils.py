import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas import DataFrame


def get_max_country(df: DataFrame) -> None:
    """
    Get the country that consumes the most products.

    Parameters:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    country_consumption = df.groupby("Country")["Quantity"].sum().reset_index()
    max_country = country_consumption.loc[country_consumption["Quantity"].idxmax()]

    print("The country that consumes the most products is:", max_country["Country"])
    print("Total quantity of products consumed:", max_country["Quantity"])


def get_most_sold_products(df: DataFrame) -> None:
    """
    Get the most sold products in terms of quantity and total sales.

    Parameters:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    df["Total_Ganancias"] = df["Quantity"] * df["Price"]

    product_sales = df.groupby("Description").agg({"Quantity": "sum", "Total_Ganancias": "sum"}).reset_index()

    most_sold_products = product_sales.sort_values(by="Quantity", ascending=False)
    most_popular_products = product_sales.sort_values(by="Total_Ganancias", ascending=False)

    print("The 10 most sold products in terms of quantity are:")
    print(most_sold_products.head(10))

    print("The 10 most popular products in terms of total sales are:")
    print(most_popular_products.head(10))


def get_trend(df: DataFrame) -> None:
    """
    Visualize the trend of total sales per month.

    Parameters:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month

    monthly_sales = df.groupby(["Year", "Month"]).agg({"Quantity": "sum"}).reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(
        monthly_sales["Month"].astype(str) + "-" + monthly_sales["Year"].astype(str),
        monthly_sales["Quantity"],
        marker="o",
        linestyle="-",
    )
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Total Sales per Month")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def get_correlation(df: DataFrame) -> None:
    """
    Calculate and visualize the correlation between price and quantity of sales.

    Parameters:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    correlation = df["Price"].corr(df["Quantity"])

    print("The correlation between price and quantity of sales is:", correlation)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="Price", y="Quantity", data=df)
    plt.xlabel("Price")
    plt.ylabel("Quantity of Sales")
    plt.title("Correlation between Price and Quantity of Sales")
    plt.grid(True)
    plt.show()
