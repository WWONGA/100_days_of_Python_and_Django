# Daily commitment
study_hours = int(input("How many hours did you study today? "))

if study_hours >= 4:
    print("✅  Excellent! You are on track.")
elif 2 <= study_hours < 4:
    print("⚠️  Try to reach 4 hours")
else:
    print("❌  You need to focus more tomorrow!")