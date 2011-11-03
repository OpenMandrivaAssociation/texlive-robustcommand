# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/robustcommand
# catalog-date 2007-02-26 15:09:49 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-robustcommand
Version:	0.1
Release:	1
Summary:	Declare robust command, with \newcommand checks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/robustcommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package merely provides a variation of
\DeclareRobustCommand, which checks for the existence of a
command before declaring it robust.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
