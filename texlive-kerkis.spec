Name:		texlive-kerkis
Version:	20180303
Release:	2
Summary:	Kerkis (Greek) font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/kerkis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kerkis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kerkis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sans-serif Greek fonts to match the URW Bookman set (which are
distributed with Kerkis). The Kerkis font set has some support
for mathematics as well as other glyphs missing from the base
URW Bookman fonts (the URW fonts are duplicated in the
distribution). Macros are provided to use the fonts in OT1, T1
(only NG/ng glyphs missing) and LGR encodings, as well as in
mathematics; small caps and old-style number glyphs are also
available. The philosophy, and the design process, of the
Kerkis fonts is discussed in a paper in TUGboat 23(3/4), 2002.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/kerkis
%{_texmfdistdir}/fonts/enc/dvips/kerkis
%{_texmfdistdir}/fonts/map/dvips/kerkis
%{_texmfdistdir}/fonts/tfm/public/kerkis
%{_texmfdistdir}/fonts/type1/public/kerkis
%{_texmfdistdir}/fonts/vf/public/kerkis
%{_texmfdistdir}/tex/latex/kerkis
%doc %{_texmfdistdir}/doc/latex/kerkis

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
