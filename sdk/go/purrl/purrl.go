// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package purrl

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/pulumiverse/pulumi-purrl/sdk/go/purrl/internal"
)

// A Pulumi provider for making API calls
type Purrl struct {
	pulumi.CustomResourceState

	// The body of the request.
	Body pulumi.StringPtrOutput `pulumi:"body"`
	// The CA certificate if server cert is not signed by a trusted CA.
	CaCert pulumi.StringPtrOutput `pulumi:"caCert"`
	// The client certificate to use for TLS verification.
	Cert pulumi.StringPtrOutput `pulumi:"cert"`
	// The body of the request.
	DeleteBody pulumi.StringPtrOutput `pulumi:"deleteBody"`
	// The CA certificate if server cert is not signed by a trusted CA.
	DeleteCaCert pulumi.StringPtrOutput `pulumi:"deleteCaCert"`
	// The client certificate to use for TLS verification.
	DeleteCert pulumi.StringPtrOutput `pulumi:"deleteCert"`
	// The headers to send with the request.
	DeleteHeaders pulumi.StringMapOutput `pulumi:"deleteHeaders"`
	// Skip TLS verification.
	DeleteInsecureSkipTLSVerify pulumi.BoolPtrOutput `pulumi:"deleteInsecureSkipTLSVerify"`
	// The client key to use for TLS verification.
	DeleteKey pulumi.StringPtrOutput `pulumi:"deleteKey"`
	// The HTTP method to use.
	DeleteMethod pulumi.StringPtrOutput `pulumi:"deleteMethod"`
	// The response from the API call.
	DeleteResponse pulumi.StringPtrOutput `pulumi:"deleteResponse"`
	// The expected response code.
	DeleteResponseCodes pulumi.StringArrayOutput `pulumi:"deleteResponseCodes"`
	// The API endpoint to call.
	DeleteUrl pulumi.StringPtrOutput `pulumi:"deleteUrl"`
	// The headers to send with the request.
	Headers pulumi.StringMapOutput `pulumi:"headers"`
	// Skip TLS verification.
	InsecureSkipTLSVerify pulumi.BoolPtrOutput `pulumi:"insecureSkipTLSVerify"`
	// The client key to use for TLS verification.
	Key pulumi.StringPtrOutput `pulumi:"key"`
	// The HTTP method to use.
	Method pulumi.StringOutput `pulumi:"method"`
	// The name for this API call.
	Name pulumi.StringOutput `pulumi:"name"`
	// The response from the API call.
	Response     pulumi.StringOutput `pulumi:"response"`
	ResponseCode pulumi.IntOutput    `pulumi:"responseCode"`
	// The expected response code.
	ResponseCodes pulumi.StringArrayOutput `pulumi:"responseCodes"`
	// The API endpoint to call.
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewPurrl registers a new resource with the given unique name, arguments, and options.
func NewPurrl(ctx *pulumi.Context,
	name string, args *PurrlArgs, opts ...pulumi.ResourceOption) (*Purrl, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Method == nil {
		return nil, errors.New("invalid value for required argument 'Method'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.ResponseCodes == nil {
		return nil, errors.New("invalid value for required argument 'ResponseCodes'")
	}
	if args.Url == nil {
		return nil, errors.New("invalid value for required argument 'Url'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Purrl
	err := ctx.RegisterResource("purrl:index:Purrl", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPurrl gets an existing Purrl resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPurrl(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PurrlState, opts ...pulumi.ResourceOption) (*Purrl, error) {
	var resource Purrl
	err := ctx.ReadResource("purrl:index:Purrl", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Purrl resources.
type purrlState struct {
}

type PurrlState struct {
}

func (PurrlState) ElementType() reflect.Type {
	return reflect.TypeOf((*purrlState)(nil)).Elem()
}

type purrlArgs struct {
	// The body of the request.
	Body *string `pulumi:"body"`
	// The CA certificate if server cert is not signed by a trusted CA.
	CaCert *string `pulumi:"caCert"`
	// The client certificate to use for TLS verification.
	Cert *string `pulumi:"cert"`
	// The body of the request.
	DeleteBody *string `pulumi:"deleteBody"`
	// The CA certificate if server cert is not signed by a trusted CA.
	DeleteCaCert *string `pulumi:"deleteCaCert"`
	// The client certificate to use for TLS verification.
	DeleteCert *string `pulumi:"deleteCert"`
	// The headers to send with the request.
	DeleteHeaders map[string]string `pulumi:"deleteHeaders"`
	// Skip TLS verification.
	DeleteInsecureSkipTLSVerify *bool `pulumi:"deleteInsecureSkipTLSVerify"`
	// The client key to use for TLS verification.
	DeleteKey *string `pulumi:"deleteKey"`
	// The HTTP method to use.
	DeleteMethod *string `pulumi:"deleteMethod"`
	// The expected response code.
	DeleteResponseCodes []string `pulumi:"deleteResponseCodes"`
	// The API endpoint to call.
	DeleteUrl *string `pulumi:"deleteUrl"`
	// The headers to send with the request.
	Headers map[string]string `pulumi:"headers"`
	// Skip TLS verification.
	InsecureSkipTLSVerify *bool `pulumi:"insecureSkipTLSVerify"`
	// The client key to use for TLS verification.
	Key *string `pulumi:"key"`
	// The HTTP method to use.
	Method string `pulumi:"method"`
	// The name for this API call.
	Name string `pulumi:"name"`
	// The expected response code.
	ResponseCodes []string `pulumi:"responseCodes"`
	// The API endpoint to call.
	Url string `pulumi:"url"`
}

// The set of arguments for constructing a Purrl resource.
type PurrlArgs struct {
	// The body of the request.
	Body pulumi.StringPtrInput
	// The CA certificate if server cert is not signed by a trusted CA.
	CaCert pulumi.StringPtrInput
	// The client certificate to use for TLS verification.
	Cert pulumi.StringPtrInput
	// The body of the request.
	DeleteBody pulumi.StringPtrInput
	// The CA certificate if server cert is not signed by a trusted CA.
	DeleteCaCert pulumi.StringPtrInput
	// The client certificate to use for TLS verification.
	DeleteCert pulumi.StringPtrInput
	// The headers to send with the request.
	DeleteHeaders pulumi.StringMapInput
	// Skip TLS verification.
	DeleteInsecureSkipTLSVerify pulumi.BoolPtrInput
	// The client key to use for TLS verification.
	DeleteKey pulumi.StringPtrInput
	// The HTTP method to use.
	DeleteMethod pulumi.StringPtrInput
	// The expected response code.
	DeleteResponseCodes pulumi.StringArrayInput
	// The API endpoint to call.
	DeleteUrl pulumi.StringPtrInput
	// The headers to send with the request.
	Headers pulumi.StringMapInput
	// Skip TLS verification.
	InsecureSkipTLSVerify pulumi.BoolPtrInput
	// The client key to use for TLS verification.
	Key pulumi.StringPtrInput
	// The HTTP method to use.
	Method pulumi.StringInput
	// The name for this API call.
	Name pulumi.StringInput
	// The expected response code.
	ResponseCodes pulumi.StringArrayInput
	// The API endpoint to call.
	Url pulumi.StringInput
}

func (PurrlArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*purrlArgs)(nil)).Elem()
}

type PurrlInput interface {
	pulumi.Input

	ToPurrlOutput() PurrlOutput
	ToPurrlOutputWithContext(ctx context.Context) PurrlOutput
}

func (*Purrl) ElementType() reflect.Type {
	return reflect.TypeOf((**Purrl)(nil)).Elem()
}

func (i *Purrl) ToPurrlOutput() PurrlOutput {
	return i.ToPurrlOutputWithContext(context.Background())
}

func (i *Purrl) ToPurrlOutputWithContext(ctx context.Context) PurrlOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PurrlOutput)
}

func (i *Purrl) ToOutput(ctx context.Context) pulumix.Output[*Purrl] {
	return pulumix.Output[*Purrl]{
		OutputState: i.ToPurrlOutputWithContext(ctx).OutputState,
	}
}

// PurrlArrayInput is an input type that accepts PurrlArray and PurrlArrayOutput values.
// You can construct a concrete instance of `PurrlArrayInput` via:
//
//	PurrlArray{ PurrlArgs{...} }
type PurrlArrayInput interface {
	pulumi.Input

	ToPurrlArrayOutput() PurrlArrayOutput
	ToPurrlArrayOutputWithContext(context.Context) PurrlArrayOutput
}

type PurrlArray []PurrlInput

func (PurrlArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Purrl)(nil)).Elem()
}

func (i PurrlArray) ToPurrlArrayOutput() PurrlArrayOutput {
	return i.ToPurrlArrayOutputWithContext(context.Background())
}

func (i PurrlArray) ToPurrlArrayOutputWithContext(ctx context.Context) PurrlArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PurrlArrayOutput)
}

func (i PurrlArray) ToOutput(ctx context.Context) pulumix.Output[[]*Purrl] {
	return pulumix.Output[[]*Purrl]{
		OutputState: i.ToPurrlArrayOutputWithContext(ctx).OutputState,
	}
}

// PurrlMapInput is an input type that accepts PurrlMap and PurrlMapOutput values.
// You can construct a concrete instance of `PurrlMapInput` via:
//
//	PurrlMap{ "key": PurrlArgs{...} }
type PurrlMapInput interface {
	pulumi.Input

	ToPurrlMapOutput() PurrlMapOutput
	ToPurrlMapOutputWithContext(context.Context) PurrlMapOutput
}

type PurrlMap map[string]PurrlInput

func (PurrlMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Purrl)(nil)).Elem()
}

func (i PurrlMap) ToPurrlMapOutput() PurrlMapOutput {
	return i.ToPurrlMapOutputWithContext(context.Background())
}

func (i PurrlMap) ToPurrlMapOutputWithContext(ctx context.Context) PurrlMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PurrlMapOutput)
}

func (i PurrlMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Purrl] {
	return pulumix.Output[map[string]*Purrl]{
		OutputState: i.ToPurrlMapOutputWithContext(ctx).OutputState,
	}
}

type PurrlOutput struct{ *pulumi.OutputState }

func (PurrlOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Purrl)(nil)).Elem()
}

func (o PurrlOutput) ToPurrlOutput() PurrlOutput {
	return o
}

func (o PurrlOutput) ToPurrlOutputWithContext(ctx context.Context) PurrlOutput {
	return o
}

func (o PurrlOutput) ToOutput(ctx context.Context) pulumix.Output[*Purrl] {
	return pulumix.Output[*Purrl]{
		OutputState: o.OutputState,
	}
}

// The body of the request.
func (o PurrlOutput) Body() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.Body }).(pulumi.StringPtrOutput)
}

// The CA certificate if server cert is not signed by a trusted CA.
func (o PurrlOutput) CaCert() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.CaCert }).(pulumi.StringPtrOutput)
}

// The client certificate to use for TLS verification.
func (o PurrlOutput) Cert() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.Cert }).(pulumi.StringPtrOutput)
}

// The body of the request.
func (o PurrlOutput) DeleteBody() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteBody }).(pulumi.StringPtrOutput)
}

// The CA certificate if server cert is not signed by a trusted CA.
func (o PurrlOutput) DeleteCaCert() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteCaCert }).(pulumi.StringPtrOutput)
}

// The client certificate to use for TLS verification.
func (o PurrlOutput) DeleteCert() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteCert }).(pulumi.StringPtrOutput)
}

// The headers to send with the request.
func (o PurrlOutput) DeleteHeaders() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringMapOutput { return v.DeleteHeaders }).(pulumi.StringMapOutput)
}

// Skip TLS verification.
func (o PurrlOutput) DeleteInsecureSkipTLSVerify() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.BoolPtrOutput { return v.DeleteInsecureSkipTLSVerify }).(pulumi.BoolPtrOutput)
}

// The client key to use for TLS verification.
func (o PurrlOutput) DeleteKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteKey }).(pulumi.StringPtrOutput)
}

// The HTTP method to use.
func (o PurrlOutput) DeleteMethod() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteMethod }).(pulumi.StringPtrOutput)
}

// The response from the API call.
func (o PurrlOutput) DeleteResponse() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteResponse }).(pulumi.StringPtrOutput)
}

// The expected response code.
func (o PurrlOutput) DeleteResponseCodes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringArrayOutput { return v.DeleteResponseCodes }).(pulumi.StringArrayOutput)
}

// The API endpoint to call.
func (o PurrlOutput) DeleteUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.DeleteUrl }).(pulumi.StringPtrOutput)
}

// The headers to send with the request.
func (o PurrlOutput) Headers() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringMapOutput { return v.Headers }).(pulumi.StringMapOutput)
}

// Skip TLS verification.
func (o PurrlOutput) InsecureSkipTLSVerify() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.BoolPtrOutput { return v.InsecureSkipTLSVerify }).(pulumi.BoolPtrOutput)
}

// The client key to use for TLS verification.
func (o PurrlOutput) Key() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringPtrOutput { return v.Key }).(pulumi.StringPtrOutput)
}

// The HTTP method to use.
func (o PurrlOutput) Method() pulumi.StringOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringOutput { return v.Method }).(pulumi.StringOutput)
}

// The name for this API call.
func (o PurrlOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The response from the API call.
func (o PurrlOutput) Response() pulumi.StringOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringOutput { return v.Response }).(pulumi.StringOutput)
}

func (o PurrlOutput) ResponseCode() pulumi.IntOutput {
	return o.ApplyT(func(v *Purrl) pulumi.IntOutput { return v.ResponseCode }).(pulumi.IntOutput)
}

// The expected response code.
func (o PurrlOutput) ResponseCodes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringArrayOutput { return v.ResponseCodes }).(pulumi.StringArrayOutput)
}

// The API endpoint to call.
func (o PurrlOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Purrl) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

type PurrlArrayOutput struct{ *pulumi.OutputState }

func (PurrlArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Purrl)(nil)).Elem()
}

func (o PurrlArrayOutput) ToPurrlArrayOutput() PurrlArrayOutput {
	return o
}

func (o PurrlArrayOutput) ToPurrlArrayOutputWithContext(ctx context.Context) PurrlArrayOutput {
	return o
}

func (o PurrlArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Purrl] {
	return pulumix.Output[[]*Purrl]{
		OutputState: o.OutputState,
	}
}

func (o PurrlArrayOutput) Index(i pulumi.IntInput) PurrlOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Purrl {
		return vs[0].([]*Purrl)[vs[1].(int)]
	}).(PurrlOutput)
}

type PurrlMapOutput struct{ *pulumi.OutputState }

func (PurrlMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Purrl)(nil)).Elem()
}

func (o PurrlMapOutput) ToPurrlMapOutput() PurrlMapOutput {
	return o
}

func (o PurrlMapOutput) ToPurrlMapOutputWithContext(ctx context.Context) PurrlMapOutput {
	return o
}

func (o PurrlMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Purrl] {
	return pulumix.Output[map[string]*Purrl]{
		OutputState: o.OutputState,
	}
}

func (o PurrlMapOutput) MapIndex(k pulumi.StringInput) PurrlOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Purrl {
		return vs[0].(map[string]*Purrl)[vs[1].(string)]
	}).(PurrlOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PurrlInput)(nil)).Elem(), &Purrl{})
	pulumi.RegisterInputType(reflect.TypeOf((*PurrlArrayInput)(nil)).Elem(), PurrlArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PurrlMapInput)(nil)).Elem(), PurrlMap{})
	pulumi.RegisterOutputType(PurrlOutput{})
	pulumi.RegisterOutputType(PurrlArrayOutput{})
	pulumi.RegisterOutputType(PurrlMapOutput{})
}
