# Quick Setup Test - Fuzzy Match Tool
import sys
print(f"✅ Python Version: {sys.version}")
print("=" * 50)

# Test core libraries
print("🔍 Testing library imports...")
print("-" * 30)

try:
    import pandas as pd
    print("✅ Pandas imported successfully")
    
    import rapidfuzz
    print(f"✅ RapidFuzz imported successfully (version: {rapidfuzz.__version__})")
    
    import streamlit as st
    print("✅ Streamlit imported successfully")
    
    import plotly
    print("✅ Plotly imported successfully")
    
    import polyfuzz
    print("✅ PolyFuzz imported successfully")
    
    import numpy as np
    print("✅ NumPy imported successfully")
    
    print("\n🎉 ALL CORE LIBRARIES INSTALLED SUCCESSFULLY!")
    print("🚀 Your development environment is ready!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 Solution: Make sure your virtual environment is activated")
    print("💡 Then run: pip install -r requirements.txt")
    exit(1)

# Test basic fuzzy matching functionality
print("\n" + "=" * 50)
print("🧠 Testing Fuzzy Matching Algorithms...")
print("-" * 35)

try:
    from rapidfuzz import fuzz
    from rapidfuzz import process
    
    # Test different algorithms
    test_cases = [
        ("hello world", "helo world"),
        ("John Smith", "Jon Smith"), 
        ("Microsoft Corporation", "Microsoft Corp"),
        ("New York", "New York City")
    ]
    
    for str1, str2 in test_cases:
        ratio = fuzz.ratio(str1, str2)
        partial = fuzz.partial_ratio(str1, str2)
        token_sort = fuzz.token_sort_ratio(str1, str2)
        
        print(f"\n🔤 Testing: '{str1}' vs '{str2}'")
        print(f"   📊 Basic Ratio: {ratio}%")
        print(f"   📊 Partial Ratio: {partial}%") 
        print(f"   📊 Token Sort: {token_sort}%")
    
    print("\n✅ Fuzzy matching algorithms are working perfectly!")
    
except Exception as e:
    print(f"❌ Fuzzy matching test failed: {e}")
    exit(1)

print("\n" + "=" * 50)
print("🎊 SETUP COMPLETE - ALL SYSTEMS GO!")
print("🚀 Ready to build your amazing fuzzy matching tool!")
print("=" * 50)
