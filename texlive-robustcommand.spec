%global tl_name robustcommand
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Declare robust command, with \newcommand checks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/robustcommand
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/robustcommand.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package merely provides a variation of \DeclareRobustCommand, which
checks for the existence of a command before declaring it robust.

