# revision 15878
# category Package
# catalog-ctan /fonts/greek/kerkis
# catalog-date 2009-01-15 17:16:29 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-kerkis
Version:	20090115
Release:	6
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
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-Bold.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-BoldSmallCaps.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-Calligraphic.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-Italic.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-SemiBold-Italic.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-SemiBold.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis-SmallCaps.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/Kerkis.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/KerkisSans-Bold.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/KerkisSans-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/KerkisSans-Italic.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/KerkisSans-SmallCaps.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/KerkisSans.afm
%{_texmfdistdir}/fonts/afm/public/kerkis/ktsy.afm
%{_texmfdistdir}/fonts/enc/dvips/kerkis/gkerkis.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/gkerkisc.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/gpkerkis.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/gpkerkisc.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kerkis.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kerkisc.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kerkisec.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kerkisecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kmath.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kmex.enc
%{_texmfdistdir}/fonts/enc/dvips/kerkis/kmsym.enc
%{_texmfdistdir}/fonts/map/dvips/kerkis/kerkis.map
%{_texmfdistdir}/fonts/tfm/public/kerkis/ek8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ek8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekbui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekcal8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekcal8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eki8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eki8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eko8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eko8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksbui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksbui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksf8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksf8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/eksfsc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ekui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gk7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gk7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkb7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbo7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbui7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkbui7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkcal7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkcal7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gki7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gki7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gko7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gko7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksb7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksbi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksbo7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksbui7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksbui7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksc7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksc7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksco7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksco7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksf7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksf7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfb7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfbi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfsc7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gksfsc7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkui7a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/gkui7t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/k8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/k8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kbui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kcal8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kcal8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ki8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ki8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kmath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kmath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ko8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ko8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksbui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksbui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksf8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksf8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ksfsc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ktsy8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/ktsy8r.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/kerkis/kui8r.tfm
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-BoldSmallCaps.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-Calligraphic.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-SemiBold-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-SemiBold.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis-SmallCaps.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/Kerkis.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/KerkisSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/KerkisSans-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/KerkisSans-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/KerkisSans-SmallCaps.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/KerkisSans.pfb
%{_texmfdistdir}/fonts/type1/public/kerkis/ktsy.pfb
%{_texmfdistdir}/fonts/vf/public/kerkis/ek8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekb8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekbi8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekbo8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekbsc8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekbsco8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekbui8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekcal8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eki8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eko8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksb8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksbi8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksbo8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksbui8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksc8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksco8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksf8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksfb8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksfbi8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksfi8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/eksfsc8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ekui8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gk7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkb7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkbi7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkbo7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkbsc8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkbsco8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkbui7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkcal7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gki7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gko7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksb7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksbi7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksbo7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksbui7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksc7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksco7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksf7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksfb7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksfbi7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksfi7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gksfsc7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/gkui7t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/k8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kb8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kbi8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kbo8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kbsc8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kbsco8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kbui8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kcal8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ki8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kmath8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ko8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksb8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksbi8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksbo8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksbui8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksc8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksco8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksf8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksfb8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksfbi8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksfi8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ksfsc8t.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/ktsy8a.vf
%{_texmfdistdir}/fonts/vf/public/kerkis/kui8a.vf
%{_texmfdistdir}/tex/latex/kerkis/kerkis.sty
%{_texmfdistdir}/tex/latex/kerkis/kmath.sty
%{_texmfdistdir}/tex/latex/kerkis/lgrkfn.fd
%{_texmfdistdir}/tex/latex/kerkis/lgrmak.fd
%{_texmfdistdir}/tex/latex/kerkis/lgrmaksf.fd
%{_texmfdistdir}/tex/latex/kerkis/omlmak.fd
%{_texmfdistdir}/tex/latex/kerkis/omsmak.fd
%{_texmfdistdir}/tex/latex/kerkis/ot1kfn.fd
%{_texmfdistdir}/tex/latex/kerkis/ot1mak.fd
%{_texmfdistdir}/tex/latex/kerkis/ot1maksf.fd
%{_texmfdistdir}/tex/latex/kerkis/t1mak.fd
%{_texmfdistdir}/tex/latex/kerkis/t1maksf.fd
%doc %{_texmfdistdir}/doc/latex/kerkis/License.txt
%doc %{_texmfdistdir}/doc/latex/kerkis/README.html

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090115-2
+ Revision: 752981
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090115-1
+ Revision: 718770
- texlive-kerkis
- texlive-kerkis
- texlive-kerkis
- texlive-kerkis

