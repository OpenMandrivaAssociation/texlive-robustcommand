Name:		texlive-robustcommand
Version:	15878
Release:	2
Summary:	Declare robust command, with \newcommand checks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/robustcommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
