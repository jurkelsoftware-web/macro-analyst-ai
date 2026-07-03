def analyze_macro_data(
    actual_nfp,
    forecast_nfp,
    previous_nfp,
    unemployment,
    forecast_unemployment,
    wage_growth,
    forecast_wage_growth,
):

    gold_score = 0
    fed_score = 0

    # Tarım Dışı İstihdam (NFP)
    if actual_nfp < forecast_nfp:
        gold_score += 3
        fed_score += 2

    # İşsizlik Oranı
    if unemployment > forecast_unemployment:
        gold_score += 1
    else:
        gold_score -= 1

    # Ortalama Saatlik Kazanç
    if wage_growth > forecast_wage_growth:
        gold_score -= 1

    return {
        "gold_score": gold_score,
        "fed_score": fed_score
    }
