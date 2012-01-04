# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tabulary
# catalog-date 2009-10-10 00:51:28 +0200
# catalog-license lppl
# catalog-version 0.9
Name:		texlive-tabulary
Version:	0.9
Release:	2
Summary:	Tabular with variable width columns balanced
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabulary
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabulary.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabulary.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabulary.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a tabular*-like tabulary environment,
taking a 'total width' argument as well as the column
specifications. It then defines column types L, C, R and J for
variable width columns (\raggedright', \centering, \raggedleft,
and normally justified). In contrast to tabularx's X columns,
the width of each column is weighted according to the natural
width of the widest cell in the column.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabulary/tabulary.sty
%doc %{_texmfdistdir}/doc/latex/tabulary/README
%doc %{_texmfdistdir}/doc/latex/tabulary/tabulary.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabulary/tabulary.dtx
%doc %{_texmfdistdir}/source/latex/tabulary/tabulary.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
