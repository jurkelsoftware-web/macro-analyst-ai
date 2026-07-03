from analyzer import analyze_macro_data

if __name__ == "__main__":
    result = analyze_macro_data(
        actual_nfp=57,
        forecast_nfp=114,
        previous_nfp=129,
        unemployment=4.2,
        forecast_unemployment=4.3,
        wage_growth=0.3,
        forecast_wage_growth=0.3,
    )

    print(result)
