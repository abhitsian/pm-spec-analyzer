# 🚀 GitHub Setup Guide

Follow these steps to upload the PM Spec Analyzer to GitHub and share with your team.

## 📋 What's Ready

Your git repository is initialized with these files:
- ✅ `app_simplified.py` - The Socratic interview app
- ✅ `README.md` - Project overview and usage
- ✅ `SETUP.md` - Step-by-step setup for team members
- ✅ `requirements.txt` - Python dependencies
- ✅ `install.sh` - One-command installation
- ✅ `run.sh` - Easy app launcher
- ✅ `.gitignore` - Excludes unnecessary files

**First commit already made!** ✅

## 🌐 Step 1: Create GitHub Repository

### Option A: Via GitHub Website (Easiest)

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `pm-spec-analyzer` (or your choice)
   - **Description**: "Socratic coach for improving PM specs through guided questioning"
   - **Visibility**:
     - ✅ **Private** (recommended for internal team tool)
     - Or **Public** (if you want to share with community)
3. **DO NOT** initialize with README (we already have one)
4. Click **"Create repository"**

### Option B: Via GitHub CLI (if installed)

```bash
gh repo create pm-spec-analyzer --private --source=. --remote=origin
```

## 📤 Step 2: Push to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add GitHub as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/pm-spec-analyzer.git

# Push the code
git branch -M main
git push -u origin main
```

**Done!** Your code is now on GitHub! 🎉

## 👥 Step 3: Share with Your Team

### Give Team Access

1. Go to your GitHub repository
2. Click **"Settings"** → **"Collaborators"**
3. Click **"Add people"**
4. Add your team members' GitHub usernames
5. They'll get an invitation email

### Share the Setup Instructions

Send your team this message:

---

**Hi team!** 👋

I've set up a Socratic coaching tool to help us write better product specs. It asks challenging questions (one at a time) to develop our thinking.

**Setup (5 minutes)**:

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pm-spec-analyzer.git
   cd pm-spec-analyzer
   ```

2. Install:
   ```bash
   ./install.sh
   ```

3. Run:
   ```bash
   ./run.sh
   ```

4. Open http://localhost:8501 in your browser

**What you need**:
- Claude Code installed (we all have this ✅)
- Python 3.8+ (most Macs have this ✅)

**How to use**:
1. Upload your spec (or paste it)
2. Start interview
3. Answer questions thoroughly
4. Get better specs!

**Time**: 10-20 minutes per spec

Check `SETUP.md` for detailed instructions and troubleshooting.

Try it with your next spec! 🎤

---

## 🔄 Updating the Tool

When you make improvements:

```bash
# Make your changes to the code

# Commit changes
git add .
git commit -m "Description of changes"

# Push to GitHub
git push
```

Team members can update their copy:
```bash
git pull
```

## 🎯 Alternative: Share Without GitHub

If your team doesn't use GitHub, you can share as a ZIP:

```bash
# Create a clean ZIP
cd ~/spec_analyzer
zip -r pm-spec-analyzer.zip \
  app_simplified.py \
  README.md \
  SETUP.md \
  requirements.txt \
  install.sh \
  run.sh

# Share pm-spec-analyzer.zip via email/Slack/etc.
```

Team members:
1. Download and extract ZIP
2. Run `./install.sh`
3. Run `./run.sh`

## 📊 Making It Even Easier

### Create a Team Repo Template

Add this to `README.md` (I've already done this):
- Clear prerequisites
- Quick start commands
- Troubleshooting section

### Record a Demo Video

1. Open the app
2. Upload a sample spec
3. Show the interview flow
4. Show the summary output

Share video with `SETUP.md` link.

### Create a Slack Channel

Create #pm-spec-analyzer channel for:
- Questions about usage
- Sharing insights from interviews
- Suggesting improvements

## ✅ Checklist

Before sharing with team:

- [ ] Repository created on GitHub
- [ ] Code pushed to GitHub
- [ ] Team members added as collaborators
- [ ] Tested that clone + install works
- [ ] Setup message prepared
- [ ] SETUP.md reviewed and accurate

## 🎓 Tips for Team Adoption

### Week 1: Soft Launch
- Share with 2-3 early adopters
- Get feedback on setup process
- Iterate on documentation

### Week 2: Broader Rollout
- Share with full team
- Demo in team meeting
- Encourage trying with next spec

### Week 3+: Habit Building
- Ask in spec reviews: "Did you run it through the coach?"
- Share examples of insights gained
- Celebrate improved specs

## 🔧 Customization

Your team can fork and customize:

### Adjust Questions

Edit `app_simplified.py` lines 109-149 to change:
- Question style (more/less challenging)
- Topics covered
- Depth of questioning

### Add Company Context

Edit lines 109-120 to add:
- ServiceNow-specific considerations
- Your team's spec template requirements
- Company-specific best practices

### Change Topics

Edit lines 46-94 (INTERVIEW_TOPICS) to:
- Add new dimensions
- Remove dimensions
- Adjust sample questions

## 📞 Support

If team members have issues:

1. Check `SETUP.md` troubleshooting section
2. Try the install steps again
3. Verify Claude Code is installed
4. Check Python version (needs 3.8+)

Most issues are:
- Claude Code not in PATH
- Python dependencies not installed
- Old Python version

## 🎉 You're Ready!

Your Socratic coaching tool is:
- ✅ Git repository initialized
- ✅ Essential files committed
- ✅ Ready to push to GitHub
- ✅ Documentation complete
- ✅ Easy setup for team

**Next step**: Create the GitHub repo and push! 🚀

Commands summary:
```bash
# Create repo on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/pm-spec-analyzer.git
git push -u origin main
```

**Then share with your team!** 👥
