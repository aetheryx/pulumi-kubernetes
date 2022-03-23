// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Core.V1
{

    /// <summary>
    /// NodeAddress contains information for the node's address.
    /// </summary>
    public class NodeAddressArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The node address.
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        /// <summary>
        /// Node address type, one of Hostname, ExternalIP or InternalIP.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public NodeAddressArgs()
        {
        }
    }
}
