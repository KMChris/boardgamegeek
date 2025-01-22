import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

st.title("Ważność zmiennych")

# Przygotowanie danych
@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def prepare_data(df):
    df = df.drop(columns=['description'])
    df = df.dropna()
    cols_float = ['complexity', 'avg_rating', 'std_rating']
    cols_int = ['year', 'min_players', 'max_players', 'min_play_time', 'max_play_time',
                'min_age', 'ratings', 'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4',
                'ratings_5', 'ratings_6', 'ratings_7', 'ratings_8', 'ratings_9',
                'ratings_10', 'comments', 'fans', 'page_views', 'plays', 'plays_month',
                'owners', 'prev_owned', 'for_trade', 'want_in_trade', 'wishlist']
    cols_list = ['alternate_names', 'designers', 'artists', 'publishers']
    df[cols_float] = df[cols_float].astype(np.float32)
    df[cols_int] = df[cols_int].astype(np.int32)
    df[cols_list] = df[cols_list].map(lambda x: [i.strip(',') for i in x])
    top_values = {
        'designers': df['designers'].explode().value_counts().nlargest(50).index,
        'artists': df['artists'].explode().value_counts().nlargest(15).index,
        'publishers': df['publishers'].explode().value_counts().nlargest(5).index
    }
    for column, top in top_values.items():
        df[column] = df[column].apply(lambda x: [column+' '+i if i in top else 'other_'+column for i in x])

    mlb = MultiLabelBinarizer()
    for column in top_values.keys():
        df = df.join(pd.DataFrame(mlb.fit_transform(df[column]), columns=mlb.classes_, index=df.index))
    df = df.drop(columns=['designers', 'artists', 'publishers'])
    X = df.drop(columns=['ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5',
                        'ratings_6', 'ratings_7', 'ratings_8', 'ratings_9', 'ratings_10',
                        'avg_rating', 'std_rating', 'name', 'alternate_names'])
    y = df[['avg_rating', 'std_rating']]
    return train_test_split(X, y, test_size=0.2, random_state=314)

X_train, X_test, y_train, y_test = prepare_data(st.session_state.df)

st.header("Ważność cech w modelu regresji liniowej")

# Model regresji liniowej
@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def linear_regression(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse_avg = mean_squared_error(y_test['avg_rating'], y_pred[:, 0])
    mse_std = mean_squared_error(y_test['std_rating'], y_pred[:, 1])
    return model.coef_, (mse_avg, mse_std)

coefs, mse = linear_regression(X_train, X_test, y_train, y_test)
st.markdown(f"""
Model regresji liniowej osiągnął następujące wyniki:
- Średni błąd kwadratowy dla średniej oceny: {mse[0]:.4f}
- Średni błąd kwadratowy dla odchylenia standardowego ocen: {mse[1]:.4f}
""")

def importance_lr(coefs, title):
    feature_importance = coefs
    feature_names = X_train.columns
    for column in ['designers', 'artists', 'publishers']:
        indices = [i for i, feature in enumerate(feature_names) if feature.startswith(column)]
        importance = feature_importance[indices].sum()
        feature_importance = np.delete(feature_importance, indices)
        feature_importance = np.append(feature_importance, importance)
        feature_names = np.delete(feature_names, indices)
        feature_names = np.append(feature_names, column)
    feature_importance = np.abs(feature_importance)
    feature_importance = feature_importance / feature_importance.sum()
    sort = np.argsort(feature_importance)
    plt.barh(feature_names[sort], feature_importance[sort])
    plt.xlabel('Ważność cech')
    plt.title(title)
    return plt.gcf()

plot = importance_lr(coefs[0], 'Ważność cech w modelu regresji liniowej dla średniej oceny')
st.pyplot(plot, clear_figure=True)
plot = importance_lr(coefs[1], 'Ważność cech w modelu regresji liniowej dla odchylenia standardowego ocen')
st.pyplot(plot, clear_figure=True)

st.header("Ważność cech w modelu gradient boosting")

# Model gradient boosting
@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def gradient_boosting(X_train, X_test, y_train, y_test):
    model = MultiOutputRegressor(GradientBoostingRegressor(random_state=314))
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse_avg = mean_squared_error(y_test['avg_rating'], y_pred[:, 0])
    mse_std = mean_squared_error(y_test['std_rating'], y_pred[:, 1])
    coef1 = model.estimators_[0].feature_importances_
    coef2 = model.estimators_[1].feature_importances_
    return (coef1, coef2), (mse_avg, mse_std)

coefs, mse = gradient_boosting(X_train, X_test, y_train, y_test)
st.markdown(f"""
Model gradient boosting osiągnął następujące wyniki:
- Średni błąd kwadratowy dla średniej oceny: {mse[0]:.4f}
- Średni błąd kwadratowy dla odchylenia standardowego ocen: {mse[1]:.4f}
""")

@st.cache_data(hash_funcs={pd.Index: lambda idx: tuple(idx)})
def importance_gb(feature_importance, title, feature_names = X_train.columns):
    for column in ['designers', 'artists', 'publishers']:
        indices = [i for i, feature in enumerate(feature_names) if feature.startswith(column)]
        importance = feature_importance[indices].sum()
        feature_importance = np.delete(feature_importance, indices)
        feature_importance = np.append(feature_importance, importance)
        feature_names = np.delete(feature_names, indices)
        feature_names = np.append(feature_names, column)
    feature_importance = np.abs(feature_importance)
    feature_importance = feature_importance / feature_importance.sum()
    sort = np.argsort(feature_importance)
    plt.barh(feature_names[sort], feature_importance[sort])
    plt.xlabel('Ważność cech')
    plt.title(title)
    return plt.gcf()

plot = importance_gb(coefs[0], 'Ważność cech w modelu Gradient Boosting dla średniej oceny')
st.pyplot(plot, clear_figure=True)
plot = importance_gb(coefs[1], 'Ważność cech w modelu Gradient Boosting dla odchylenia standardowego ocen')
st.pyplot(plot, clear_figure=True)
