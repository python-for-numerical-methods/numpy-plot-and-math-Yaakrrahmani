import numpy as np

def normalized_array(arr_in):
    # המרת הקלט למערך נומפאי מטיפוס float64
    vector = np.asarray(arr_in, dtype=np.float64)
    
    # בדיקת מגן למקרה של מערך ללא איברים
    if vector.size == 0:
        return np.array([])
    
    # שליפת ערכי הקצה של המערך
    minimum = vector.min()
    maximum = vector.max()
    
    # חישוב הטווח - מונע חלוקה באפס במידה וכל הערכים זהים
    variance_range = maximum - minimum
    if variance_range == 0:
        return np.zeros_like(vector)
    
    # נרמול הערכים לטווח של 0-1
    normalized_output = (vector - minimum) / variance_range
    return normalized_output

if __name__ == "__main__":
    # בדיקה מקומית
    demo_data = [10, 20, 30, 40, 50]
    print(f"Original: {demo_data}")
    print(f"Result:   {normalized_array(demo_data)}")
