# 🔧 Troubleshooting: Word Document Upload

## Issue: Analyze Button Disabled After Uploading Word Doc

### ✅ Fixed! Better Error Messages Added

I've updated the app with **improved error handling** that will tell you exactly what's wrong.

---

## 🚀 Try Again Now

The app has been **restarted with better error messages**.

### Steps:

1. **Refresh your browser** at http://localhost:8501

2. **Check the sidebar** - It will now show:
   - ✅ **Word Support: Enabled** (if working)
   - ⚠️ **Word Support: Not available** (if broken)

3. **Upload a Word doc** and you'll see specific error messages:
   - If Word support is missing
   - If the document is empty
   - If there's an encoding error
   - What to do to fix it

---

## 🧪 Test With Sample Document

I've created a test Word document for you:

**Location**: `/tmp/test_spec.docx`

### Test It:

1. Go to the app: http://localhost:8501
2. Click **"Upload File"**
3. Navigate to `/tmp/` in the file picker
4. Select `test_spec.docx`
5. Should see: "✅ Extracted XX characters from Word document"

If this works, the issue is with your specific Word document!

---

## 🔍 Common Issues & Solutions

### Issue 1: "Word document support not available"

**Cause**: python-docx not installed in Streamlit environment

**Fix**:
```bash
pipx inject streamlit python-docx
# Then restart app
pkill -f streamlit
cd ~/spec_analyzer
streamlit run app.py
```

### Issue 2: "Word document appears to be empty"

**Causes**:
- Document only contains images (can't extract text from images)
- Document has text in text boxes (not extracted)
- Document is actually empty

**Fix**:
- Save document as .txt and upload that
- Or copy-paste content into "Paste Text" mode

### Issue 3: Button Still Disabled

**Check these**:
- Is "Your Name" filled in? ✓
- Is "Spec Title" filled in? ✓
- Is "Spec Preview" showing text? ✓

All three must have content for button to enable!

### Issue 4: File Encoding Error

**Cause**: Text file not in UTF-8 format

**Fix**:
- Save as .docx instead (handles encoding automatically)
- Or save text file as UTF-8 in your editor

---

## 📋 Verification Checklist

Test if Word support is working:

- [ ] Refresh browser at http://localhost:8501
- [ ] Check sidebar shows "✅ Word Support: Enabled"
- [ ] Upload `/tmp/test_spec.docx`
- [ ] See success message with character count
- [ ] See spec preview with extracted text
- [ ] Analyze button becomes enabled
- [ ] Click analyze and get results

If all checks pass, Word support is working! ✅

---

## 🔧 Debug: Check Word Support Manually

Test the extraction directly:

```bash
# Test in Streamlit's Python environment
~/.local/pipx/venvs/streamlit/bin/python << 'EOF'
from docx import Document
doc = Document('/tmp/test_spec.docx')
text = '\n'.join([p.text for p in doc.paragraphs])
print(f"Extracted {len(text)} characters")
print("Preview:", text[:200])
EOF
```

Should show extracted text without errors.

---

## 💡 Workarounds

If Word upload still doesn't work:

### Option 1: Use Paste Text Mode
1. Open your Word doc
2. Select All (Cmd+A)
3. Copy (Cmd+C)
4. In app, select "Paste Text"
5. Paste (Cmd+V)
6. Analyze!

### Option 2: Save as Text
1. In Word: File → Save As
2. Format: Plain Text (.txt)
3. Upload the .txt file

### Option 3: Use Markdown
1. In Word: File → Save As
2. Format: Markdown (.md) if available
3. Upload the .md file

---

## 🎯 What You Should See

### Working Word Upload:

```
Upload Spec Document
[Browse files] ← Click here
test_spec.docx selected ✓

✅ Extracted 156 characters from Word document

Spec Preview:
[Shows extracted text]

[🔍 Analyze Spec] ← Button is ENABLED
```

### Broken Word Upload:

```
Upload Spec Document
[Browse files] ← Click here
test_spec.docx selected ✓

❌ Error reading file: [specific error]
💡 Try: 1) Saving as .txt or .md, or 2) Copy-pasting

[🔍 Analyze Spec] ← Button is DISABLED (greyed out)
```

---

## 📞 Still Not Working?

### Collect Debug Info:

1. **Sidebar status**: What does it say about Word Support?
2. **Error message**: What exact error do you see?
3. **File details**: What's the filename and size?
4. **Test document**: Does `/tmp/test_spec.docx` work?

### Quick Reset:

```bash
# Reinstall Word support
pipx inject streamlit python-docx --force

# Restart app
pkill -f streamlit
cd ~/spec_analyzer
streamlit run app.py

# Refresh browser
open http://localhost:8501
```

---

## ✅ Current Status

**App State**:
- ✅ Restarted with better error messages
- ✅ Created test document at `/tmp/test_spec.docx`
- ✅ python-docx installed in Streamlit venv
- ✅ Improved error handling shows specific issues

**Next Steps**:
1. Refresh browser
2. Check sidebar for Word Support status
3. Try test document first
4. Then try your actual Word doc
5. Read any error messages shown

---

**The app is ready - refresh your browser and try the test document!** 🚀
