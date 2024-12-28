from scipy.stats import spearmanr
def spearman_rank_correlation(x, y):
    return spearmanr(x, y).correlation
study_hours = [2, 4, 6, 8, 10]
exam_scores = [50, 55, 65, 75, 85]
print("Spearman Rank Correlation:", spearman_rank_correlation(study_hours, exam_scores))
