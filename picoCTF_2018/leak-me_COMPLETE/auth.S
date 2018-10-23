
auth:	file format ELF32-i386

Disassembly of section .init:
_init:
 804845c:	53 	pushl	%ebx
 804845d:	83 ec 08 	subl	$8, %esp
 8048460:	e8 2b 01 00 00 	calll	299 <__x86.get_pc_thunk.bx>
 8048465:	81 c3 9b 1b 00 00 	addl	$7067, %ebx
 804846b:	8b 83 fc ff ff ff 	movl	-4(%ebx), %eax
 8048471:	85 c0 	testl	%eax, %eax
 8048473:	74 05 	je	5 <_init+0x1e>
 8048475:	e8 d6 00 00 00 	calll	214
 804847a:	83 c4 08 	addl	$8, %esp
 804847d:	5b 	popl	%ebx
 804847e:	c3 	retl
Disassembly of section .plt:
.plt:
 8048480:	ff 35 04 a0 04 08 	pushl	134520836
 8048486:	ff 25 08 a0 04 08 	jmpl	*134520840
 804848c:	00 00 	addb	%al, (%eax)
 804848e:	00 00 	addb	%al, (%eax)
 8048490:	ff 25 0c a0 04 08 	jmpl	*134520844
 8048496:	68 00 00 00 00 	pushl	$0
 804849b:	e9 e0 ff ff ff 	jmp	-32 <.plt>
 80484a0:	ff 25 10 a0 04 08 	jmpl	*134520848
 80484a6:	68 08 00 00 00 	pushl	$8
 80484ab:	e9 d0 ff ff ff 	jmp	-48 <.plt>
 80484b0:	ff 25 14 a0 04 08 	jmpl	*134520852
 80484b6:	68 10 00 00 00 	pushl	$16
 80484bb:	e9 c0 ff ff ff 	jmp	-64 <.plt>
 80484c0:	ff 25 18 a0 04 08 	jmpl	*134520856
 80484c6:	68 18 00 00 00 	pushl	$24
 80484cb:	e9 b0 ff ff ff 	jmp	-80 <.plt>
 80484d0:	ff 25 1c a0 04 08 	jmpl	*134520860
 80484d6:	68 20 00 00 00 	pushl	$32
 80484db:	e9 a0 ff ff ff 	jmp	-96 <.plt>
 80484e0:	ff 25 20 a0 04 08 	jmpl	*134520864
 80484e6:	68 28 00 00 00 	pushl	$40
 80484eb:	e9 90 ff ff ff 	jmp	-112 <.plt>
 80484f0:	ff 25 24 a0 04 08 	jmpl	*134520868
 80484f6:	68 30 00 00 00 	pushl	$48
 80484fb:	e9 80 ff ff ff 	jmp	-128 <.plt>
 8048500:	ff 25 28 a0 04 08 	jmpl	*134520872
 8048506:	68 38 00 00 00 	pushl	$56
 804850b:	e9 70 ff ff ff 	jmp	-144 <.plt>
 8048510:	ff 25 2c a0 04 08 	jmpl	*134520876
 8048516:	68 40 00 00 00 	pushl	$64
 804851b:	e9 60 ff ff ff 	jmp	-160 <.plt>
 8048520:	ff 25 30 a0 04 08 	jmpl	*134520880
 8048526:	68 48 00 00 00 	pushl	$72
 804852b:	e9 50 ff ff ff 	jmp	-176 <.plt>
 8048530:	ff 25 34 a0 04 08 	jmpl	*134520884
 8048536:	68 50 00 00 00 	pushl	$80
 804853b:	e9 40 ff ff ff 	jmp	-192 <.plt>
 8048540:	ff 25 38 a0 04 08 	jmpl	*134520888
 8048546:	68 58 00 00 00 	pushl	$88
 804854b:	e9 30 ff ff ff 	jmp	-208 <.plt>
Disassembly of section .plt.got:
.plt.got:
 8048550:	ff 25 fc 9f 04 08 	jmpl	*134520828
 8048556:	66 90 	nop
Disassembly of section .text:
_start:
 8048560:	31 ed 	xorl	%ebp, %ebp
 8048562:	5e 	popl	%esi
 8048563:	89 e1 	movl	%esp, %ecx
 8048565:	83 e4 f0 	andl	$-16, %esp
 8048568:	50 	pushl	%eax
 8048569:	54 	pushl	%esp
 804856a:	52 	pushl	%edx
 804856b:	68 30 89 04 08 	pushl	$134514992
 8048570:	68 d0 88 04 08 	pushl	$134514896
 8048575:	51 	pushl	%ecx
 8048576:	56 	pushl	%esi
 8048577:	68 c8 86 04 08 	pushl	$134514376
 804857c:	e8 7f ff ff ff 	calll	-129 <.plt+0x80>
 8048581:	f4 	hlt
 8048582:	66 90 	nop
 8048584:	66 90 	nop
 8048586:	66 90 	nop
 8048588:	66 90 	nop
 804858a:	66 90 	nop
 804858c:	66 90 	nop
 804858e:	66 90 	nop

__x86.get_pc_thunk.bx:
 8048590:	8b 1c 24 	movl	(%esp), %ebx
 8048593:	c3 	retl
 8048594:	66 90 	nop
 8048596:	66 90 	nop
 8048598:	66 90 	nop
 804859a:	66 90 	nop
 804859c:	66 90 	nop
 804859e:	66 90 	nop

deregister_tm_clones:
 80485a0:	b8 47 a0 04 08 	movl	$134520903, %eax
 80485a5:	2d 44 a0 04 08 	subl	$134520900, %eax
 80485aa:	83 f8 06 	cmpl	$6, %eax
 80485ad:	76 1a 	jbe	26 <deregister_tm_clones+0x29>
 80485af:	b8 00 00 00 00 	movl	$0, %eax
 80485b4:	85 c0 	testl	%eax, %eax
 80485b6:	74 11 	je	17 <deregister_tm_clones+0x29>
 80485b8:	55 	pushl	%ebp
 80485b9:	89 e5 	movl	%esp, %ebp
 80485bb:	83 ec 14 	subl	$20, %esp
 80485be:	68 44 a0 04 08 	pushl	$134520900
 80485c3:	ff d0 	calll	*%eax
 80485c5:	83 c4 10 	addl	$16, %esp
 80485c8:	c9 	leave
 80485c9:	f3 c3 	rep		retl
 80485cb:	90 	nop
 80485cc:	8d 74 26 00 	leal	(%esi), %esi

register_tm_clones:
 80485d0:	b8 44 a0 04 08 	movl	$134520900, %eax
 80485d5:	2d 44 a0 04 08 	subl	$134520900, %eax
 80485da:	c1 f8 02 	sarl	$2, %eax
 80485dd:	89 c2 	movl	%eax, %edx
 80485df:	c1 ea 1f 	shrl	$31, %edx
 80485e2:	01 d0 	addl	%edx, %eax
 80485e4:	d1 f8 	sarl	%eax
 80485e6:	74 1b 	je	27 <register_tm_clones+0x33>
 80485e8:	ba 00 00 00 00 	movl	$0, %edx
 80485ed:	85 d2 	testl	%edx, %edx
 80485ef:	74 12 	je	18 <register_tm_clones+0x33>
 80485f1:	55 	pushl	%ebp
 80485f2:	89 e5 	movl	%esp, %ebp
 80485f4:	83 ec 10 	subl	$16, %esp
 80485f7:	50 	pushl	%eax
 80485f8:	68 44 a0 04 08 	pushl	$134520900
 80485fd:	ff d2 	calll	*%edx
 80485ff:	83 c4 10 	addl	$16, %esp
 8048602:	c9 	leave
 8048603:	f3 c3 	rep		retl
 8048605:	8d 74 26 00 	leal	(%esi), %esi
 8048609:	8d bc 27 00 00 00 00 	leal	(%edi), %edi

__do_global_dtors_aux:
 8048610:	80 3d 68 a0 04 08 00 	cmpb	$0, 134520936
 8048617:	75 13 	jne	19 <__do_global_dtors_aux+0x1c>
 8048619:	55 	pushl	%ebp
 804861a:	89 e5 	movl	%esp, %ebp
 804861c:	83 ec 08 	subl	$8, %esp
 804861f:	e8 7c ff ff ff 	calll	-132 <deregister_tm_clones>
 8048624:	c6 05 68 a0 04 08 01 	movb	$1, 134520936
 804862b:	c9 	leave
 804862c:	f3 c3 	rep		retl
 804862e:	66 90 	nop

frame_dummy:
 8048630:	b8 10 9f 04 08 	movl	$134520592, %eax
 8048635:	8b 10 	movl	(%eax), %edx
 8048637:	85 d2 	testl	%edx, %edx
 8048639:	75 05 	jne	5 <frame_dummy+0x10>
 804863b:	eb 93 	jmp	-109 <register_tm_clones>
 804863d:	8d 76 00 	leal	(%esi), %esi
 8048640:	ba 00 00 00 00 	movl	$0, %edx
 8048645:	85 d2 	testl	%edx, %edx
 8048647:	74 f2 	je	-14 <frame_dummy+0xb>
 8048649:	55 	pushl	%ebp
 804864a:	89 e5 	movl	%esp, %ebp
 804864c:	83 ec 14 	subl	$20, %esp
 804864f:	50 	pushl	%eax
 8048650:	ff d2 	calll	*%edx
 8048652:	83 c4 10 	addl	$16, %esp
 8048655:	c9 	leave
 8048656:	e9 75 ff ff ff 	jmp	-139 <register_tm_clones>

flag:
 804865b:	55 	pushl	%ebp
 804865c:	89 e5 	movl	%esp, %ebp
 804865e:	83 ec 48 	subl	$72, %esp
 8048661:	83 ec 08 	subl	$8, %esp
 8048664:	68 50 89 04 08 	pushl	$134515024
 8048669:	68 52 89 04 08 	pushl	$134515026
 804866e:	e8 ad fe ff ff 	calll	-339 <.plt+0xa0>
 8048673:	83 c4 10 	addl	$16, %esp
 8048676:	89 45 f4 	movl	%eax, -12(%ebp)
 8048679:	83 7d f4 00 	cmpl	$0, -12(%ebp)
 804867d:	75 1a 	jne	26 <flag+0x3e>
 804867f:	83 ec 0c 	subl	$12, %esp
 8048682:	68 5c 89 04 08 	pushl	$134515036
 8048687:	e8 44 fe ff ff 	calll	-444 <.plt+0x50>
 804868c:	83 c4 10 	addl	$16, %esp
 804868f:	83 ec 0c 	subl	$12, %esp
 8048692:	6a 00 	pushl	$0
 8048694:	e8 47 fe ff ff 	calll	-441 <.plt+0x60>
 8048699:	83 ec 04 	subl	$4, %esp
 804869c:	ff 75 f4 	pushl	-12(%ebp)
 804869f:	6a 30 	pushl	$48
 80486a1:	8d 45 c4 	leal	-60(%ebp), %eax
 80486a4:	50 	pushl	%eax
 80486a5:	e8 06 fe ff ff 	calll	-506 <.plt+0x30>
 80486aa:	83 c4 10 	addl	$16, %esp
 80486ad:	83 ec 08 	subl	$8, %esp
 80486b0:	8d 45 c4 	leal	-60(%ebp), %eax
 80486b3:	50 	pushl	%eax
 80486b4:	68 d1 89 04 08 	pushl	$134515153
 80486b9:	e8 e2 fd ff ff 	calll	-542 <.plt+0x20>
 80486be:	83 c4 10 	addl	$16, %esp
 80486c1:	b8 00 00 00 00 	movl	$0, %eax
 80486c6:	c9 	leave
 80486c7:	c3 	retl

main:
 80486c8:	8d 4c 24 04 	leal	4(%esp), %ecx
 80486cc:	83 e4 f0 	andl	$-16, %esp
 80486cf:	ff 71 fc 	pushl	-4(%ecx)
 80486d2:	55 	pushl	%ebp
 80486d3:	89 e5 	movl	%esp, %ebp
 80486d5:	57 	pushl	%edi
 80486d6:	51 	pushl	%ecx
 80486d7:	81 ec 90 01 00 00 	subl	$400, %esp
 80486dd:	a1 64 a0 04 08 	movl	134520932, %eax
 80486e2:	6a 00 	pushl	$0
 80486e4:	6a 02 	pushl	$2
 80486e6:	6a 00 	pushl	$0
 80486e8:	50 	pushl	%eax
 80486e9:	e8 22 fe ff ff 	calll	-478 <.plt+0x90>
 80486ee:	83 c4 10 	addl	$16, %esp
 80486f1:	e8 ca fd ff ff 	calll	-566 <.plt+0x40>
 80486f6:	89 45 f4 	movl	%eax, -12(%ebp)
 80486f9:	83 ec 04 	subl	$4, %esp
 80486fc:	ff 75 f4 	pushl	-12(%ebp)
 80486ff:	ff 75 f4 	pushl	-12(%ebp)
 8048702:	ff 75 f4 	pushl	-12(%ebp)
 8048705:	e8 36 fe ff ff 	calll	-458 <.plt+0xc0>
 804870a:	83 c4 10 	addl	$16, %esp
 804870d:	83 ec 04 	subl	$4, %esp
 8048710:	6a 40 	pushl	$64
 8048712:	6a 00 	pushl	$0
 8048714:	8d 45 ac 	leal	-84(%ebp), %eax
 8048717:	50 	pushl	%eax
 8048718:	e8 13 fe ff ff 	calll	-493 <.plt+0xb0>
 804871d:	83 c4 10 	addl	$16, %esp
 8048720:	83 ec 04 	subl	$4, %esp
 8048723:	68 00 01 00 00 	pushl	$256
 8048728:	6a 00 	pushl	$0
 804872a:	8d 85 ac fe ff ff 	leal	-340(%ebp), %eax
 8048730:	50 	pushl	%eax
 8048731:	e8 fa fd ff ff 	calll	-518 <.plt+0xb0>
 8048736:	83 c4 10 	addl	$16, %esp
 8048739:	83 ec 04 	subl	$4, %esp
 804873c:	6a 40 	pushl	$64
 804873e:	6a 00 	pushl	$0
 8048740:	8d 85 6c fe ff ff 	leal	-404(%ebp), %eax
 8048746:	50 	pushl	%eax
 8048747:	e8 e4 fd ff ff 	calll	-540 <.plt+0xb0>
 804874c:	83 c4 10 	addl	$16, %esp
 804874f:	83 ec 0c 	subl	$12, %esp
 8048752:	68 d4 89 04 08 	pushl	$134515156
 8048757:	e8 74 fd ff ff 	calll	-652 <.plt+0x50>
 804875c:	83 c4 10 	addl	$16, %esp
 804875f:	a1 60 a0 04 08 	movl	134520928, %eax
 8048764:	83 ec 04 	subl	$4, %esp
 8048767:	50 	pushl	%eax
 8048768:	68 00 01 00 00 	pushl	$256
 804876d:	8d 85 ac fe ff ff 	leal	-340(%ebp), %eax
 8048773:	50 	pushl	%eax
 8048774:	e8 37 fd ff ff 	calll	-713 <.plt+0x30>
 8048779:	83 c4 10 	addl	$16, %esp
 804877c:	83 ec 08 	subl	$8, %esp
 804877f:	6a 0a 	pushl	$10
 8048781:	8d 85 ac fe ff ff 	leal	-340(%ebp), %eax
 8048787:	50 	pushl	%eax
 8048788:	e8 63 fd ff ff 	calll	-669 <.plt+0x70>
 804878d:	83 c4 10 	addl	$16, %esp
 8048790:	89 45 f0 	movl	%eax, -16(%ebp)
 8048793:	83 7d f0 00 	cmpl	$0, -16(%ebp)
 8048797:	74 06 	je	6 <main+0xd7>
 8048799:	8b 45 f0 	movl	-16(%ebp), %eax
 804879c:	c6 00 00 	movb	$0, (%eax)
 804879f:	8d 85 ac fe ff ff 	leal	-340(%ebp), %eax
 80487a5:	b9 ff ff ff ff 	movl	$4294967295, %ecx
 80487aa:	89 c2 	movl	%eax, %edx
 80487ac:	b8 00 00 00 00 	movl	$0, %eax
 80487b1:	89 d7 	movl	%edx, %edi
 80487b3:	f2 ae 	repne		scasb	%es:(%edi), %al
 80487b5:	89 c8 	movl	%ecx, %eax
 80487b7:	f7 d0 	notl	%eax
 80487b9:	8d 50 ff 	leal	-1(%eax), %edx
 80487bc:	8d 85 ac fe ff ff 	leal	-340(%ebp), %eax
 80487c2:	01 d0 	addl	%edx, %eax
 80487c4:	c7 00 2c 0a 50 6c 	movl	$1817184812, (%eax)
 80487ca:	c7 40 04 65 61 73 65 	movl	$1702060389, 4(%eax)
 80487d1:	c7 40 08 20 45 6e 74 	movl	$1953383712, 8(%eax)
 80487d8:	c7 40 0c 65 72 20 74 	movl	$1948283493, 12(%eax)
 80487df:	c7 40 10 68 65 20 50 	movl	$1344300392, 16(%eax)
 80487e6:	c7 40 14 61 73 73 77 	movl	$2004054881, 20(%eax)
 80487ed:	c7 40 18 6f 72 64 2e 	movl	$778334831, 24(%eax)
 80487f4:	c6 40 1c 00 	movb	$0, 28(%eax)
 80487f8:	83 ec 08 	subl	$8, %esp
 80487fb:	68 50 89 04 08 	pushl	$134515024
 8048800:	68 e7 89 04 08 	pushl	$134515175
 8048805:	e8 16 fd ff ff 	calll	-746 <.plt+0xa0>
 804880a:	83 c4 10 	addl	$16, %esp
 804880d:	89 45 ec 	movl	%eax, -20(%ebp)
 8048810:	83 7d ec 00 	cmpl	$0, -20(%ebp)
 8048814:	75 1a 	jne	26 <main+0x168>
 8048816:	83 ec 0c 	subl	$12, %esp
 8048819:	68 f4 89 04 08 	pushl	$134515188
 804881e:	e8 ad fc ff ff 	calll	-851 <.plt+0x50>
 8048823:	83 c4 10 	addl	$16, %esp
 8048826:	83 ec 0c 	subl	$12, %esp
 8048829:	6a 00 	pushl	$0
 804882b:	e8 b0 fc ff ff 	calll	-848 <.plt+0x60>
 8048830:	83 ec 04 	subl	$4, %esp
 8048833:	ff 75 ec 	pushl	-20(%ebp)
 8048836:	6a 40 	pushl	$64
 8048838:	8d 45 ac 	leal	-84(%ebp), %eax
 804883b:	50 	pushl	%eax
 804883c:	e8 6f fc ff ff 	calll	-913 <.plt+0x30>
 8048841:	83 c4 10 	addl	$16, %esp
 8048844:	83 ec 0c 	subl	$12, %esp
 8048847:	68 6d 8a 04 08 	pushl	$134515309
 804884c:	e8 4f fc ff ff 	calll	-945 <.plt+0x20>
 8048851:	83 c4 10 	addl	$16, %esp
 8048854:	83 ec 0c 	subl	$12, %esp
 8048857:	8d 85 ac fe ff ff 	leal	-340(%ebp), %eax
 804885d:	50 	pushl	%eax
 804885e:	e8 6d fc ff ff 	calll	-915 <.plt+0x50>
 8048863:	83 c4 10 	addl	$16, %esp
 8048866:	a1 60 a0 04 08 	movl	134520928, %eax
 804886b:	83 ec 04 	subl	$4, %esp
 804886e:	50 	pushl	%eax
 804886f:	6a 40 	pushl	$64
 8048871:	8d 85 6c fe ff ff 	leal	-404(%ebp), %eax
 8048877:	50 	pushl	%eax
 8048878:	e8 33 fc ff ff 	calll	-973 <.plt+0x30>
 804887d:	83 c4 10 	addl	$16, %esp
 8048880:	c6 85 ac fe ff ff 00 	movb	$0, -340(%ebp)
 8048887:	83 ec 08 	subl	$8, %esp
 804888a:	8d 45 ac 	leal	-84(%ebp), %eax
 804888d:	50 	pushl	%eax
 804888e:	8d 85 6c fe ff ff 	leal	-404(%ebp), %eax
 8048894:	50 	pushl	%eax
 8048895:	e8 f6 fb ff ff 	calll	-1034 <.plt+0x10>
 804889a:	83 c4 10 	addl	$16, %esp
 804889d:	85 c0 	testl	%eax, %eax
 804889f:	75 07 	jne	7 <main+0x1e0>
 80488a1:	e8 b5 fd ff ff 	calll	-587 <flag>
 80488a6:	eb 10 	jmp	16 <main+0x1f0>
 80488a8:	83 ec 0c 	subl	$12, %esp
 80488ab:	68 74 8a 04 08 	pushl	$134515316
 80488b0:	e8 1b fc ff ff 	calll	-997 <.plt+0x50>
 80488b5:	83 c4 10 	addl	$16, %esp
 80488b8:	b8 00 00 00 00 	movl	$0, %eax
 80488bd:	8d 65 f8 	leal	-8(%ebp), %esp
 80488c0:	59 	popl	%ecx
 80488c1:	5f 	popl	%edi
 80488c2:	5d 	popl	%ebp
 80488c3:	8d 61 fc 	leal	-4(%ecx), %esp
 80488c6:	c3 	retl
 80488c7:	66 90 	nop
 80488c9:	66 90 	nop
 80488cb:	66 90 	nop
 80488cd:	66 90 	nop
 80488cf:	90 	nop

__libc_csu_init:
 80488d0:	55 	pushl	%ebp
 80488d1:	57 	pushl	%edi
 80488d2:	56 	pushl	%esi
 80488d3:	53 	pushl	%ebx
 80488d4:	e8 b7 fc ff ff 	calll	-841 <__x86.get_pc_thunk.bx>
 80488d9:	81 c3 27 17 00 00 	addl	$5927, %ebx
 80488df:	83 ec 0c 	subl	$12, %esp
 80488e2:	8b 6c 24 20 	movl	32(%esp), %ebp
 80488e6:	8d b3 0c ff ff ff 	leal	-244(%ebx), %esi
 80488ec:	e8 6b fb ff ff 	calll	-1173 <_init>
 80488f1:	8d 83 08 ff ff ff 	leal	-248(%ebx), %eax
 80488f7:	29 c6 	subl	%eax, %esi
 80488f9:	c1 fe 02 	sarl	$2, %esi
 80488fc:	85 f6 	testl	%esi, %esi
 80488fe:	74 25 	je	37 <__libc_csu_init+0x55>
 8048900:	31 ff 	xorl	%edi, %edi
 8048902:	8d b6 00 00 00 00 	leal	(%esi), %esi
 8048908:	83 ec 04 	subl	$4, %esp
 804890b:	ff 74 24 2c 	pushl	44(%esp)
 804890f:	ff 74 24 2c 	pushl	44(%esp)
 8048913:	55 	pushl	%ebp
 8048914:	ff 94 bb 08 ff ff ff 	calll	*-248(%ebx,%edi,4)
 804891b:	83 c7 01 	addl	$1, %edi
 804891e:	83 c4 10 	addl	$16, %esp
 8048921:	39 f7 	cmpl	%esi, %edi
 8048923:	75 e3 	jne	-29 <__libc_csu_init+0x38>
 8048925:	83 c4 0c 	addl	$12, %esp
 8048928:	5b 	popl	%ebx
 8048929:	5e 	popl	%esi
 804892a:	5f 	popl	%edi
 804892b:	5d 	popl	%ebp
 804892c:	c3 	retl
 804892d:	8d 76 00 	leal	(%esi), %esi

__libc_csu_fini:
 8048930:	f3 c3 	rep		retl
Disassembly of section .fini:
_fini:
 8048934:	53 	pushl	%ebx
 8048935:	83 ec 08 	subl	$8, %esp
 8048938:	e8 53 fc ff ff 	calll	-941 <__x86.get_pc_thunk.bx>
 804893d:	81 c3 c3 16 00 00 	addl	$5827, %ebx
 8048943:	83 c4 08 	addl	$8, %esp
 8048946:	5b 	popl	%ebx
 8048947:	c3 	retl
