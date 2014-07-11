# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/robustcommand
# catalog-date 2007-02-26 15:09:49 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-robustcommand
Version:	0.1
Release:	8
Summary:	Declare robust command, with \newcommand checks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/robustcommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package merely provides a variation of
\DeclareRobustCommand, which checks for the existence of a
command before declaring it robust.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/robustcommand/robustcommand.sty
%doc %{_texmfdistdir}/doc/latex/robustcommand/README
%doc %{_texmfdistdir}/doc/latex/robustcommand/robustcommand.pdf
#- source
%doc %{_texmfdistdir}/source/latex/robustcommand/robustcommand.dtx
%doc %{_texmfdistdir}/source/latex/robustcommand/robustcommand.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 755718
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719457
- texlive-robustcommand
- texlive-robustcommand
- texlive-robustcommand
- texlive-robustcommand

