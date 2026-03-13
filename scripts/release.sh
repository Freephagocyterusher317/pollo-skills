#!/usr/bin/env bash
set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Ensure we're in a git repo
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  echo -e "${RED}Error: not a git repository${NC}"
  exit 1
fi

# Ensure working tree is clean
if [ -n "$(git status --porcelain)" ]; then
  echo -e "${RED}Error: working tree is not clean. Commit or stash changes first.${NC}"
  exit 1
fi

# Ensure we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
  echo -e "${RED}Error: releases must be created from the main branch (current: ${CURRENT_BRANCH})${NC}"
  exit 1
fi

# Get latest tag
LATEST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
echo -e "${BOLD}Current version: ${CYAN}${LATEST_TAG}${NC}"
echo ""

# Parse semver
VERSION="${LATEST_TAG#v}"
IFS='.' read -r MAJOR MINOR PATCH <<< "$VERSION"

# Calculate next versions
NEXT_PATCH="v${MAJOR}.${MINOR}.$((PATCH + 1))"
NEXT_MINOR="v${MAJOR}.$((MINOR + 1)).0"
NEXT_MAJOR="v$((MAJOR + 1)).0.0"

# Present options
echo -e "${BOLD}Select version bump:${NC}"
echo ""
echo -e "  ${GREEN}1)${NC} patch  → ${CYAN}${NEXT_PATCH}${NC}"
echo -e "  ${GREEN}2)${NC} minor  → ${CYAN}${NEXT_MINOR}${NC}"
echo -e "  ${GREEN}3)${NC} major  → ${CYAN}${NEXT_MAJOR}${NC}"
echo ""

# Read choice
while true; do
  read -rp "$(echo -e "${BOLD}Your choice [1-3]: ${NC}")" CHOICE
  case "$CHOICE" in
    1) NEXT_VERSION="$NEXT_PATCH"; break ;;
    2) NEXT_VERSION="$NEXT_MINOR"; break ;;
    3) NEXT_VERSION="$NEXT_MAJOR"; break ;;
    *) echo -e "${RED}Invalid choice. Please enter 1, 2, or 3.${NC}" ;;
  esac
done

echo ""
echo -e "${YELLOW}Will create tag: ${BOLD}${NEXT_VERSION}${NC}"
read -rp "$(echo -e "${BOLD}Confirm? [y/N]: ${NC}")" CONFIRM
if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
  echo -e "${RED}Aborted.${NC}"
  exit 0
fi

# Create and push tag
git tag -a "$NEXT_VERSION" -m "Release $NEXT_VERSION"
git push origin "$NEXT_VERSION"

echo ""
echo -e "${GREEN}✅ Tag ${BOLD}${NEXT_VERSION}${GREEN} created and pushed.${NC}"
echo -e "${GREEN}   GitHub Actions will create the release automatically.${NC}"
