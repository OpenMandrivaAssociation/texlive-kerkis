%global tl_name kerkis
%global tl_revision 56271
%global tl_version 1.11

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Kerkis (Greek) font family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/kerkis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kerkis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kerkis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Sans-serif Greek fonts to match the URW Bookman set (which are
distributed with Kerkis). The Kerkis font set has some support for
mathematics as well as other glyphs missing from the base URW Bookman
fonts. Macros are provided to use the fonts in OT1, T1 (only NG/ng
glyphs missing) and LGR encodings, as well as in mathematics; small caps
and old-style number glyphs are also available. The philosophy, and the
design process, of the Kerkis fonts is discussed in a paper in TUGboat
23(3/4), 2002.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from kerkis:
Map kerkis.map
TL_DROPIN_EOF
