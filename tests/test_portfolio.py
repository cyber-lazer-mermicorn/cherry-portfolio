"""Tests for Cherry Portfolio — validates HTML structure and content."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_index_html_exists():
    html = ROOT / "index.html"
    assert html.exists(), "index.html missing"
    print("PASS: test_index_html_exists")


def test_html_has_doctype():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "<!DOCTYPE html>" in content, "Missing DOCTYPE"
    print("PASS: test_html_has_doctype")


def test_html_has_title():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "<title>" in content, "Missing title tag"
    title_match = re.search(r"<title>(.*?)</title>", content)
    assert title_match, "Title tag empty"
    assert "Cherry" in title_match.group(1), "Title missing name"
    print("PASS: test_html_has_title")


def test_html_has_meta_description():
    html = ROOT / "index.html"
    content = html.read_text()
    assert 'name="description"' in content, "Missing meta description"
    print("PASS: test_html_has_meta_description")


def test_html_has_og_tags():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "og:title" in content, "Missing og:title"
    assert "og:description" in content, "Missing og:description"
    assert "og:image" in content, "Missing og:image"
    print("PASS: test_html_has_og_tags")


def test_html_has_viewport():
    html = ROOT / "index.html"
    content = html.read_text()
    assert 'viewport' in content, "Missing viewport meta"
    print("PASS: test_html_has_viewport")


def test_html_has_navigation():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "<nav" in content, "Missing navigation"
    print("PASS: test_html_has_navigation")


def test_html_has_hero():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "hero" in content.lower(), "Missing hero section"
    print("PASS: test_html_has_hero")


def test_html_has_projects_section():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "Projects" in content or "projects" in content, "Missing projects section"
    print("PASS: test_html_has_projects_section")


def test_html_has_contact():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "mailto:" in content or "contact" in content.lower(), "Missing contact info"
    print("PASS: test_html_has_contact")


def test_html_has_footer():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "<footer" in content, "Missing footer"
    print("PASS: test_html_has_footer")


def test_html_is_responsive():
    html = ROOT / "index.html"
    content = html.read_text()
    assert "@media" in content, "Missing media queries (not responsive)"
    print("PASS: test_html_is_responsive")


def test_html_has_no_broken_links():
    html = ROOT / "index.html"
    content = html.read_text()
    # Check for empty hrefs
    empty_hrefs = re.findall(r'href=""', content)
    assert len(empty_hrefs) == 0, f"Found {len(empty_hrefs)} empty hrefs"
    print("PASS: test_html_has_no_broken_links")


def test_sitemap_exists():
    sitemap = ROOT / "sitemap.xml"
    assert sitemap.exists(), "sitemap.xml missing"
    content = sitemap.read_text()
    assert "urlset" in content or "sitemapindex" in content, "Invalid sitemap"
    print("PASS: test_sitemap_exists")


def test_robots_exists():
    robots = ROOT / "robots.txt"
    assert robots.exists(), "robots.txt missing"
    print("PASS: test_robots_exists")


def test_no_secrets_in_html():
    html = ROOT / "index.html"
    content = html.read_text()
    secret_patterns = [r"ghp_[A-Za-z0-9]{36}", r"sk-[A-Za-z0-9]{48}"]
    for pattern in secret_patterns:
        assert not re.search(pattern, content), f"Secret found in index.html"
    print("PASS: test_no_secrets_in_html")


def test_deploy_script_exists():
    deploy = ROOT / "deploy-portfolio.sh"
    assert deploy.exists(), "deploy-portfolio.sh missing"
    print("PASS: test_deploy_script_exists")


def test_readme_exists():
    readme = ROOT / "README.md"
    assert readme.exists(), "README.md missing"
    print("PASS: test_readme_exists")


def run_all():
    tests = [
        test_index_html_exists,
        test_html_has_doctype,
        test_html_has_title,
        test_html_has_meta_description,
        test_html_has_og_tags,
        test_html_has_viewport,
        test_html_has_navigation,
        test_html_has_hero,
        test_html_has_projects_section,
        test_html_has_contact,
        test_html_has_footer,
        test_html_is_responsive,
        test_html_has_no_broken_links,
        test_sitemap_exists,
        test_robots_exists,
        test_no_secrets_in_html,
        test_deploy_script_exists,
        test_readme_exists,
    ]
    passed = failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    return failed == 0


if __name__ == "__main__":
    import sys
    sys.exit(0 if run_all() else 1)
