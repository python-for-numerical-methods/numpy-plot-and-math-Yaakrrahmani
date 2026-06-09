import numpy as np

def rescale_features(data_input):
    """
    מבצע נרמול מינימום-מקסימום (Min-Max Scaling) לטווח של 0 עד 1.
    """
    # המרה למערך נומפאי עם תמיכה במספרים עשרוניים
    x = np.asarray(data_input, dtype=np.float64)
    
    # טיפול במערך ריק באמצעות תכונת ה-size
    if x.size == 0:
        return np.empty(0)
        
    # שליפת ערכי המינימום והמקסימום ישירות מהאובייקט
    low, high = x.min(), x.max()
    span = high - low
    
    # מניעת חלוקה באפס במידה וכל האיברים במערך זהים
    if span == 0:
        return np.zeros_like(x)
        
    # חישוב הטווח המנורמל והחזרת התוצאה
    return (x - low) / span

if __name__ == "__main__":
    # בדיקת תקינות הלוגיקה
    test_values = [10, 20, 30, 40, 50]
    normalized_values = rescale_features(test_values)
    
    print(f"Original: {test_values}")
    print(f"Scaled:   {normalized_values}")
